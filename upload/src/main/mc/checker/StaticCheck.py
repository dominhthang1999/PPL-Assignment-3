
"""
 * Do Minh Thang
 * 1713217
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [

    #Built in Function
        Symbol("getInt", MType([], IntType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn",MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType()))
    ]

    # list of name function unreachable
    unreached = []
    __currentFunction = 0
    __funcType = None

    def __init__(self,ast):
        self.ast = ast

    #default return None.
    #If it has exists, return Symbol of the sepecified name in the environment.
    # name: String
    # env: List or tuple of Symbol
    def findSymbol(self, name, env):
        result = None
        if type(env) is tuple:
            for i in env:
                if result is None:
                    result = self.lookup(name, i, lambda x: x.name)
        else:
            result = self.lookup(name, env, lambda x: x.name)
        return result

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi[:])

    def typeCheck(self, x, y):
        if type(x) == type(y):
            if type(x) is ArrayType and x.eleType != y.eleType:
                return False
            else:
                return True
        else:
            if type(x) is FloatType and type(y) is IntType:
                return True
            else:
                return False

    # c[0] is the environment or tuple of environment
    # c[1] is kind of the visit
    def visitProgram(self, ast, c):
        # g = c[:]
        g = [c]

        # This loop will visit all of variable global and function and save it into g
        for x in ast.decl:
            if type(x) is VarDecl:
                g[0] += [self.visit(x, g)]
            else:
                if self.findSymbol(x, g):
                    raise Redeclared(Function(), x.name.name)
                g[0] += [Symbol(x.name.name, MType([j for j in x.partype], x.rettype),False)]

        # mainFunc = self.findSymbol('main', g)
        # if mainFunc is None or (type(mainFunc.mtype) != MType):
        #     raise NoEntryPoint();

        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, g)
        mainFunc = self.findSymbol('main', g)
        if mainFunc is None or (type(mainFunc.mtype) != MType):
            raise NoEntryPoint();
        if len(self.unreached) > 0:
            raise UnreachableFunction(self.unreached[0].name)
        return ""

    # param is a list of list
    # param[0] is the environment
    def visitVarDecl(self, ast, params):
        res = Symbol(ast.variable, ast.varType)
        check = self.findSymbol(ast.variable, params[0])
        if check is None:
            params[0].append(res)
            return res
        else:
            raise Redeclared(Variable(), res.name)

    # param: list of parameter type in current function
    def visitFuncDecl(self, ast, params):

        localEnvironment = [[]] + params
        for i in ast.param:
            if self.findSymbol(i.variable, localEnvironment[0]):
                raise Redeclared(Parameter(), i.variable)
            localEnvironment[0] += [Symbol(i.variable, i.varType)]
        checkReturn = False
        for i in ast.body.member:
            if type(i) is VarDecl:
                localEnvironment[0] += [self.visit(i, localEnvironment)]
            else:
                checkReturn = self.visit(i, localEnvironment) or checkReturn
        if checkReturn is False:
            raise FunctionNotReturn(ast.name.name)

    # If a statement contains Return Statement in all its flow, it must return the returnType, otherwise None
    # Since there params[1] is the returnType of the current function.
    # params[2]: can be missing or None, or set to 'loop' when visit statements inside a loop
    def visitAndGetReturnType(self, stmtList, params):
        returnCheck = []

        if type(stmtList) == list:
            for stmt in stmtList:

                temp = self.visit(stmt, params)

                if temp is None or type(temp) is Symbol:
                    returnCheck.append(temp)
                else:
                    returnCheck.append('Returned')

        else:
            temp = self.visit(stmtList, params)
            if temp is None:
                returnCheck.append(temp)
            else:
                returnCheck.append('Returned')
        if type(params[1]) is VoidType: return params[1]
        return None if not 'Returned' in returnCheck else params[1]

    ######################################
    # Statements that can contain others #
    ######################################

    def visitIf(self, ast, params):
        exprIf = self.visit(ast.expr, params)
        if not type(exprIf) is BoolType:
            raise TypeMismatchInStatement(ast.expr.name)
        checkThen = False
        checkElse = False
        # checkThen = self.visitAndGetReturnType(ast.thenStmt, params)
        checkThen = self.visit(ast.thenStmt, params) or checkThen
        if not ast.elseStmt is None:
            # checkElse = self.visitAndGetReturnType(ast.elseStmt, params)
            checkElse = self.visit(ast.elseStmt, params) or checkElse
            if checkElse is True and checkThen is True:
                return True
            return False
            # return None if checkThen is None and checkElse is None else params[1]
        # return None if checkThen is None else params[1]
        return False

    def visitFor(self, ast, params):
        expr1 = self.visit(ast.expr1, params)
        expr2 = self.visit(ast.expr2, params)
        expr3 = self.visit(ast.expr3, params)

        if not type(expr1) is IntType or not type(expr3) is IntType or not type(expr2) is BoolType:
            raise TypeMismatchInStatement(ast)
        loop = self.visit(ast.loop, params)
        return False

    def visitDowhile(self, ast, params):
        exp = self.visit(ast.exp, params)

        if not type(exp) is BoolType:
            raise TypeMismatchInStatement(ast)
        checkRet = False
        for stmt in ast.sl:
            checkRet = self.visit(stmt, params) or checkRet
        return checkRet


    #####################
    # Single statements #
    #####################

    def visitContinue(self, ast, params):
        if self.__currentInLoop == 0:
            raise ContinueNotInLoop()
        return False

    def visitBreak(self, ast, params):
        if self.__currentInLoop == 0:
            raise BreakNotInLoop()
        return False

    def visitReturn(self, ast, params):
        if ast.expr is None:
            if not type(params[1]) is VoidType:
                raise TypeMismatchInStatement(ast)
            return None
        else:
            exp = self.visit(ast.expr, params[0])
            if self.typeCheck(params[1], exp) is None:
                raise TypeMismatchInStatement(ast)
            return exp

    #################################################
    # Expressions only use params[0] as environment #
    #################################################

    def visitCallExpr(self, ast, enviroment):
        callParam = []

        for i in ast.param:
            callParam += [self.visit(i, enviroment[:])]

        for i in enviroment:
            res = self.findSymbol(ast.method.name, i)
            if res:
                if type(res.mtype) is MType:
                    if len(callParam) != len(ast.mtype.partype):
                        raise TypeMismatchInExpression(ast)
                    Pairs = list(zip(callParam, ast.mtype.partype))
                    for pair in Pairs:
                        if type(pair[0]) != type(pair[1]):
                            if type(pair[0]) is IntType and type(pair[1]) is FloatType:
                                pass
                            else:
                                raise TypeMismatchInExpression(ast)
                        else:
                            if type(pair[0]) is ArrayType:
                                if type(pair[0].eleType) == type(pair[1].eleType)
                                    pass
                                else:
                                    raise TypeMismatchInExpression(ast)
                    return res.mtype.rettype

                else:
                    raise TypeMismatchInExpression(ast)
        raise Undeclared(Function(), ast.method.name)



    def visitBinaryOp(self, ast, enviroment):

        left = self.visit(ast.left, enviroment)
        right = self.visit(ast.right, enviroment)
        if type(ast.left) not in (Id, ArrayCell) and ast.op == "=":
             raise NotLeftValue(ast.left)

        if type(left) != type(right):
            if type(left) is IntType and type(right) is FloatType:
                left, right = right, left
            elif type(left) is FloatType and type(right) is IntType: pass
            else:
                raise TypeMismatchInExpression(ast)
        if type(left) is BoolType:
            if ast.op in ("==", "!=", "&&", "||", "="):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        if type(left) is IntType:

            if ast.op == "/":
                return FloatType()
            if ast.op in ("+", "-", "*", "%", "="):
                return IntType()
            if ast.op in ("<", "<=", ">", ">=", "==", "!="):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        if type(left) is FloatType:
            if ast.op in ("+", "-", "*", "/", "="):
                return IntType()
            if ast.op in ("<", "<=", ">", ">="):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        if type(left) is StringType:
            if ast.op == "=":
                return StringType()
            raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, enviroment):
        exp = self.visit(ast.body, enviroment)
        if (ast.op == "!" and type(exp) is BoolType)\
            or (ast.op == "-" and type(exp) in (IntType, FloatType)):
            return exp
        raise TypeMismatchInExpression


    # type ast is symbol
    def visitId(self, ast, enviroment):
        print(enviroment)
        for i in enviroment:
            checkId = self.findSymbol(ast.name, i)
            if checkId.mtype is MType:
                return checkId.mtype.rettype
            else:
                return checkId.mtype
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, enviroment):
        index = self.visit(ast.idx, enviroment)
        if not type(index) is IntType:
            raise TypeMismatchInExpression(ast)
        array = self.visit(ast.arr, enviroment)
        if not type(array) is ArrayType:
            raise TypeMismatchInStatement(ast)
        else:
            return array.eleType

    def visitBlock(self, ast, enviroment):
        [self.visit(x, enviroment) for x in ast.member]
        return None

    ##############
    # visit Type #
    ##############

    def visitArrayPointerType(self, ast, params):
        pass

    def visitIntLiteral(self, ast, params):
        return IntType()

    def visitFloatLiteral(self, ast, params):
        return FloatType()

    def visitBooleanLiteral(self, ast, params):
        return BoolType()

    def visitStringLiteral(self, ast, params):
        return StringType()
