# import unittest
# from TestUtils import TestChecker
# from AST import *

# class CheckSuite(unittest.TestCase):
#     #Redeclared Error
#     def test_redeclared_global_variable(self):
#         input = """
#         int a;
#         int a;
#         void main(){}
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,400))

#     def test_redeclared_variable_function(self):
#         input = """
#         int main;
#         void main(){}
#         """
#         expect = "Redeclared Function: main"
#         self.assertTrue(TestChecker.test(input,expect,401))

#     def test_redeclared_local_variable(self):
#         input = """
#         int b;
#         void main(){
#             int a;
#             int a;
#         }"""
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,402))

#     def test_redeclared_function(self):
#         input = """
#         int a(){}
#         void a(){}
#         void main(){}
#         """
#         expect = "Redeclared Function: a"
#         self.assertTrue(TestChecker.test(input,expect,403))

#     def test_redeclared_parameter(self):
#         input = """
#         void main(int c, int c){}"""
#         expect = "Redeclared Parameter: c"
#         self.assertTrue(TestChecker.test(input,expect,404))

#     def test_redeclared_parameter_local_variable(self):
#         input = """
#         void main(int a){
#             int a;
#         }"""
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,405))

#     def test_redeclared_block_variable(self):
#         input = """
#         void main(){
#             {
#                 int a;
#                 int a;
#             }
#         }"""
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,406))

#     def test_redeclared_block_block_variable(self):
#         input = """
#         void main(){
#             int a;
#             {
#                 int a;
#                 {
#                     int b;
#                     int b;
#                 }
#             }
#         }"""
#         expect = "Redeclared Variable: b"
#         self.assertTrue(TestChecker.test(input,expect,407))

#     def test_redeclared_arraytype(self):
#         input = """
#         void main(){
#             int a[5];
#             int a[3];
#         }
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,408))

#     def test_redeclared_variable_arraytype(self):
#         input = """
#         void main(){
#             int a;
#             int a[10];
#         }
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,409))

#     #Undeclared Error
#     def test_undeclared_global_variable(self):
#         input = """
#         int a;
#         void main(){
#             b = 5;
#         }
#         """
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input,expect,410))

#     def test_undeclared_ifstmt_expr(self):
#         input = """
#         void main(){
#             int b;
#             if (a > 5) b = 5;
#         }
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,411))

#     def test_undeclared_forstmt_expr(self):
#         input = """
#         void main(){
#             int b;
#             for (i; i < 10; i = i + 1){
#                 b = b + 1;
#             }
#         }
#         """
#         expect = "Undeclared Identifier: i"
#         self.assertTrue(TestChecker.test(input,expect,412))

#     def test_undeclared_dowhilestmt_expr(self):
#         input = """
#         void main(){
#             int b;
#             do a = 5; b = b + 1; while(b == 0);
#         }
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,413))

#     def test_undeclared_returnstmt_expr(self):
#         input = """
#         void main(){
#             return a;
#         }
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,414))

#     def test_undeclared_function_priority(self):
#         input = """
#         void main(){
#             foo();
#         }
#         void fo(){
#             f();
#         }
#         """
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,415))

#     def test_undeclared_function_binaryop_expr(self):
#         input = """
#         void main(){
#             int a;
#             a = foo(3)[3];
#         }
#         """
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,416))

#     def test_undeclared_function_infunction(self):
#         input = """
#         int foo(int a){
#             return 1;
#         }
#         void main(){
#             int a;
#             a = foo(fo(1));
#         }
#         """
#         expect = "Undeclared Function: fo"
#         self.assertTrue(TestChecker.test(input,expect,417))

#     def test_undeclared_identifier_function_priority(self):
#         input = """
#         void main(){
#             a = foo();
#         }
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input,expect,418))

#     def test_undeclared_function_identifier_priority(self):
#         input = """
#         void main(){
#             foo() = a;
#         }
#         """
#         expect = "Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,419))

#     def test_typemismatchstatement_ifstmt(self):
#         input = """
#         void main(){
#             int a;
#             if (a) a = 2;
#         }
#         """
#         expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),IntLiteral(2)))"
#         self.assertTrue(TestChecker.test(input,expect,420))

#     def test_typemismatchstatement_forstmt_expr2(self):
#         input = """
#         void main(){
#             int a;
#             for (a; a+1; a = a + 1){
#                 a = 0;
#             }
#         }
#         """
#         expect = "Type Mismatch In Statement: For(Id(a);BinaryOp(+,Id(a),IntLiteral(1));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([BinaryOp(=,Id(a),IntLiteral(0))]))"
#         self.assertTrue(TestChecker.test(input,expect,421))

#     def test_typemismatchstatement_forstmt_expr1(self):
#         input = """
#         void main(){
#             int a;
#             for (a/1.0; a > 10; a = a + 1){
#                 a = 0;
#             }
#         }
#         """
#         expect = "Type Mismatch In Statement: For(BinaryOp(/,Id(a),FloatLiteral(1.0));BinaryOp(>,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([BinaryOp(=,Id(a),IntLiteral(0))]))"
#         self.assertTrue(TestChecker.test(input,expect,422))

#     def test_typemismatchstatement_forstmt_expr3(self):
#         input = """
#         void main(){
#             int a;
#             for (a/1; a > 10; a == a + 1){
#                 a = 0;
#             }
#         }
#         """
#         expect = "Type Mismatch In Statement: For(BinaryOp(/,Id(a),IntLiteral(1));BinaryOp(>,Id(a),IntLiteral(10));BinaryOp(==,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([BinaryOp(=,Id(a),IntLiteral(0))]))"
#         self.assertTrue(TestChecker.test(input,expect,423))

#     def test_typemismatchstatement_dowhilestmt_expr(self):
#         input = """
#         void main(){
#             int a;
#             do a = 3; while(a);
#         }
#         """
#         expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),IntLiteral(3))],Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,424))

#     def test_typemismatchstatement_returnstmt_voidtype(self):
#         input = """
#         void main(){
#             int a;
#             return a;
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,425))

#     def test_typemismatchstatement_returnstmt_inttype(self):
#         input = """
#         float foo(){
#             return 1;
#         }
#         int main(){
#             float a;
#             return foo();
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))"
#         self.assertTrue(TestChecker.test(input,expect,426))

#     def test_typemismatchstatement_returnstmt_string_arraypointertype(self):
#         input = """
#         string[] SO(string a[]){
#             string b;
#             return b;
#         }
#         void main(){
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,427))

#     def test_typemismatchstatement_returnstmt_string_arraytype(self):
#         input = """
#         boolean S(string a[]){
#             boolean b[5];
#             return b;
#         }
#         void main(){
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,428))

#     def test_typemismatchstatement_binaryop_forstmt(self):
#         input = """
#         void main(){
#             int a;
#             for (a = 1; a > 10; --a){
#                 if (a) a = 0;
#                 else a = 1;
#             }
#         }
#         """
#         expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),IntLiteral(0)),BinaryOp(=,Id(a),IntLiteral(1)))"
#         self.assertTrue(TestChecker.test(input,expect,429))

#     #TypeMismatchExpression Error
#     def test_typemismatchexpress_arraytype_E1(self):
#         input = """
#         void main(){
#             int a;
#             a[2] = 1;
#         }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
#         self.assertTrue(TestChecker.test(input,expect,430))

#     def test_typemismatchexpress_arraytype_E2(self):
#         input = """
#         void main(){
#             int a[1];
#             a[a] = 1;
#         }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,431))

#     def test_typemismatchexpress_arraypointertype(self):
#         input = """
#         int foo(int a[]){
#             a = 0;
#             return a[1];
#         }
#         void main(){
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(0))"
#         self.assertTrue(TestChecker.test(input,expect,432))

#     def test_typemismatchexpress_binaryexpression_arraypointertype(self):
#         input = """
#         void main(int b[]){
#             int a;
#             b = a;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,433))

#     def test_typemismatchexpress_binaryexpression_arraytype(self):
#         input = """
#         void main(){
#             int a[1];
#             a = 1;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
#         self.assertTrue(TestChecker.test(input,expect,434))

#     def test_typemismatchexpress_binaryexpression_booltype(self):
#         input = """
#         void main(){
#             boolean a;
#             int b;
#             b = a + 1;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"
#         self.assertTrue(TestChecker.test(input,expect,435))

#     def test_typemismatchexpress_binaryexpression_booltype_ifstmt(self):
#         input = """
#         void main(){
#             boolean a;
#             int b;
#             if (a + 1) b = 1;
#             else b = 0;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"
#         self.assertTrue(TestChecker.test(input,expect,436))

#     def test_typemismatchexpress_binaryexpression_inttype(self):
#         input = """
#         void main(){
#             int a;
#             int b;
#             b = b == a;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(==,Id(b),Id(a)))"
#         self.assertTrue(TestChecker.test(input,expect,437))

#     def test_typemismatchexpress_binaryexpression_inttype_ifstmt(self):
#         input = """
#         void main(){
#             int a;
#             float b;
#             if(b == a) a = 1;
#             else a = 0;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,438))

#     def test_typemismatchexpress_binaryexpression_floattype(self):
#         input = """
#         void main(){
#             float a;
#             float b;
#             boolean c;
#             c = b == a;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,439))

#     def test_typemismatchexpress_binaryexpression_floattype_ifstmt(self):
#         input = """
#         void main(){
#             float a;
#             float b;
#             if(b == a) a = 1;
#             else a = 0;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,440))

#     def test_typemismatchexpress_binaryexpression_floattype_unaryop(self):
#         input = """
#         void main(){
#             int a;
#             float b;
#             a = -b;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),UnaryOp(-,Id(b)))"
#         self.assertTrue(TestChecker.test(input,expect,441))

#     def test_typemismatchexpress_binaryexpression_stringtype(self):
#         input = """
#         void main(){
#             string a;
#             string b;
#             a = a + b;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,442))

#     def test_typemismatchexpress_binaryexpression_stringtype_ifstmt(self):
#         input = """
#         void main(){
#             string a;
#             string b;
#             if (a == b) a == "a";
#             else a == "b";
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,443))

#     def test_typemismatchexpress_functioncall_notparam(self):
#         input = """
#         int foo(){
#             return 1;
#         }
#         void main(){
#             int a;
#             a = foo(2);
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(2)])"
#         self.assertTrue(TestChecker.test(input,expect,444))

#     def test_typemismatchexpress_functioncall_notparamtype(self):
#         input = """
#         int foo(int a){
#             return 1;
#         }
#         void main(){
#             int a;
#             float b;
#             a = foo(b);
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(b)])"
#         self.assertTrue(TestChecker.test(input,expect,445))

#     def test_typemismatchexpress_functioncall_notparamtype_arraypointertype(self):
#         input = """
#         int foo(int a[]){
#             return 1;
#         }
#         void main(){
#             int a;
#             int b[1];
#             a = foo(b[1]);
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(b),IntLiteral(1))])"
#         self.assertTrue(TestChecker.test(input,expect,446))

#     def test_typemismatchexpress_functioncall_notparamtype_arraytype(self):
#         input = """
#         int foo(int a[]){
#             return 1;
#         }
#         void main(){
#             int a;
#             int b[1];
#             b[1] = foo(a);
#         }
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
#         self.assertTrue(TestChecker.test(input,expect,447))

#     def test_typemismatchexpress_binaryop_mod(self):
#         input = """
#         void main(){
#             float a;
#             int b;
#             b = a % b;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,448))

#     def test_typemismatchexpress_binaryop_div(self):
#         input = """
#         void main(){
#             float a;
#             int b;
#             b = a / b;
#         }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(/,Id(a),Id(b)))"
#         self.assertTrue(TestChecker.test(input,expect,449))

#     #Functionnotreturn Error
#     def test_functionnotreturn(self):
#         input = """
#         int main(){
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,450))

#     def test_functionnotreturn_function(self):
#         input = """
#         int foo(){
#         }
#         void main(){
#         }
#         """
#         expect = "Function foo Not Return "
#         self.assertTrue(TestChecker.test(input,expect,451))

#     def test_functionnotreturn_ifstmt_noelsestmt(self):
#         input = """
#         int main(){
#             int a;
#             if (true) return 1;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,452))

#     def test_functionnotreturn_ifstmt_elsestmt(self):
#         input = """
#         int main(){
#             int a;
#             if (true) return 1;
#             else a = 1;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,453))

#     def test_functionnotreturn_noifstmt_elsestmt(self):
#         input = """
#         int main(){
#             int a;
#             if (true) a = 1;
#             else return a;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,454))

#     def test_functionnotreturn_forstmt(self):
#         input = """
#         int main(){
#             int a;
#             for (a = 1; a > 10; --a) return a;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,455))

#     def test_functionnotreturn_forstmt_block(self):
#         input = """
#         int main(){
#             int a;
#             for (a = 1; a > 10; --a) {
#                 if (a == 1) return 1;
#                 else return 2;
#             }
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,456))

#     def test_functionnotreturn_dowhilestmt(self):
#         input = """
#         int main(){
#             int a;
#             do a = 1; while(a != 1);
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,457))

#     def test_functionnotreturn_dowhilestmt_block(self):
#         input = """
#         int main(){
#             int a;
#             do {
#                 for (a = 1; a < 0; a = a + 1) return 1;
#             } while(a != 1);
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,458))

#     def test_functionnotreturn_dowhilestmt_block_ifstmt(self):
#         input = """
#         int main(){
#             int a;
#             do {
#                 for (a = 1; a < 0; a = a + 1) return 1;
#             } while(a != 1);
#             if (a == 1) return 1;
#         }
#         """
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,459))

#     def test_breaknotinloop_dowhilestmt(self):
#         input = """
#         int main(){
#             int a;
#             do {
#                 for (a = 1; a < 0; a = a + 1) return 1;
#                 return 2;
#             } while(a != 1);
#             break;
#             return 1;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,460))

#     def test_breaknotinloop(self):
#         input = """
#         int main(){
#             break;
#             return 1;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,461))

#     def test_breaknotinloop_ifstmt(self):
#         input = """
#         int main(){
#             int a;
#             if (a == 1) break;
#             return 1;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,462))

#     def test_breaknotinloop_forstmt_ifstmt(self):
#         input = """
#         int main(){
#             int a;
#             if (a == 1) {
#                 for (a = 1; a < 10; --a) {
#                     a = a + 1;
#                 }
#                 break;
#             }
#             return 1;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,463))

#     def test_breaknotinloop_dowhilestmt_ifstmt(self):
#         input = """
#         int main(){
#             int a;
#             if (a == 1) {
#                 do a = a + 1; while (a < 10);
#                 break;
#             }
#             return 1;
#         }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,464))

#     def test_continuenotinloop_dowhilestmt(self):
#         input = """
#         int main(){
#             int a;
#             do {
#                 for (a = 1; a < 0; a = a + 1) return 1;
#                 return 2;
#             } while(a != 1);
#             continue;
#             return 1;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,465))

#     def test_continuenotinloop(self):
#         input = """
#         int main(){
#             continue;
#             return 1;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,466))

#     def test_continuenotinloop_ifstmt(self):
#         input = """
#         int main(){
#             int a;
#             if (a == 1) continue;
#             return 1;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,467))

#     def test_continuenotinloop_forstmt_ifstmt(self):
#         input = """
#         int main(){
#             int a;
#             if (a == 1) {
#                 for (a = 1; a < 10; --a) {
#                     a = a + 1;
#                     break;
#                 }
#                 continue;
#             }
#             return 1;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,468))

#     def test_continuenotinloop_dowhilestmt_ifstmt(self):
#         input = """
#         int main(){
#             int a;
#             if (a == 1) {
#                 do a = a + 1; break; while (a < 10);
#                 continue;
#             }
#             return 1;
#         }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,469))

#     #Noentrypoint Error
#     def test_noentrypoint(self):
#         input = """
#         int foo(){}
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,470))

#     def test_noentrypoint_global_variable(self):
#         input = """
#         int main;
#         int noentrypoint(){}
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,471))

#     def test_noentrypoint_global_variable_main(self):
#         input = """
#         int main;
#         int mai(){
#             int main;
#         }
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,472))

#     def test_noentrypoint_local_variable_main(self):
#         input = """
#         int foo(){
#             int main;
#         }
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,473))

#     def test_noentrypoint_local_variable_main_thisis(self):
#         input = """
#         int thisisnotmain(){
#             int thisismainvariable;
#         }
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,474))

#     #Unreachablefunction Error
#     def test_unreachablefunction(self):
#         input = """
#         int foo(int a){
#             fo();
#             return 1;
#         }
#         void fo(){}
#         void main(){
#             int a;
#         }
#         """
#         expect = "Unreachable Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,475))

#     def test_unreachablefunction_priority(self):
#         input = """
#         int foo(){
#             return 1;
#         }
#         void fo(){}
#         void main(){
#             int a;
#         }
#         """
#         expect = "Unreachable Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,476))

#     def test_unreachablefunction_priority_aftermainfunction(self):
#         input = """
#         void main(){
#             int a;
#         }
#         int foo(){
#             return 1;
#         }
#         void fo(){}
#         """
#         expect = "Unreachable Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,477))

#     def test_unreachablefunction_priority_global_variable(self):
#         input = """
#         void main(){
#             int a;
#         }
#         int b;
#         void foo(){
#             b = 2;
#         }
#         """
#         expect = "Unreachable Function: foo"
#         self.assertTrue(TestChecker.test(input,expect,478))

#     def test_unreachablefunction_priority_global_variable_priority(self):
#         input = """
#         void fo(){
#         }
#         void main(){
#             int a;
#         }
#         int b;
#         void foo(){
#             b = 2;
#         }
#         """
#         expect = "Unreachable Function: fo"
#         self.assertTrue(TestChecker.test(input,expect,479))

#     #Noleftvalue
#     def test_noleftvalue_inttype(self):
#         input = """
#         void main(){
#             int a;
#             2 = a;
#         }
#         """
#         expect = "Not Left Value: IntLiteral(2)"
#         self.assertTrue(TestChecker.test(input,expect,480))

#     def test_noleftvalue_floattype(self):
#         input = """
#         void main(){
#             float a[4];
#             26.9 = a[2];
#         }
#         """
#         expect = "Not Left Value: FloatLiteral(26.9)"
#         self.assertTrue(TestChecker.test(input,expect,481))

#     def test_noleftvalue_stringtype(self):
#         input = """
#         void main(){
#             string a;
#             "a" = a;
#         }
#         """
#         expect = "Not Left Value: StringLiteral(a)"
#         self.assertTrue(TestChecker.test(input,expect,482))

#     def test_noleftvalue_booltype(self):
#         input = """
#         void main(){
#             boolean a[3];
#             true = a[1];
#         }
#         """
#         expect = "Not Left Value: BooleanLiteral(true)"
#         self.assertTrue(TestChecker.test(input,expect,483))

#     def test_noleftvalue_random(self):
#         input = """
#         void main(int a[]){
#             int b;
#             28.8 = b;
#         }
#         """
#         expect = "Not Left Value: FloatLiteral(28.8)"
#         self.assertTrue(TestChecker.test(input,expect,484))

#     #Random Error
#     def test_random_dowhilestmt(self):
#         input ="""void main(){
#             int a;
#             int b;
#             a = 1;
#             b = 0;
#             do {a = a + 1.0; b = b - 1;
#             } while a <= 10 && b > -10 ;
#         }"""
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.0)))"
#         self.assertTrue(TestChecker.test(input,expect,485))

#     def test_random_forstmt(self):
#         input = """int main(){
#             int i, a[5];
#             int i, j, a[5];
#             for (i = 10; i > 0; --i) {
#                 for (j = 0; j < i; j = j + 1)
#                     a[i] = j; a[0] = 0;
#             }
#         }"""
#         expect = "Redeclared Variable: i"
#         self.assertTrue(TestChecker.test(input,expect,486))

#     def test_ifstmt_10(self):
#         input = """int main(){
#             string a;
#             boolean b;
#             if (a == "a") b = true;
#             else {
#                 if (a == "b") b = false;
#                 else {a = "c";
#                 }
#             }
#         }"""
#         expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),StringLiteral(a))"
#         self.assertTrue(TestChecker.test(input,expect,487))

#     def test_random_breakstmt(self):
#         input = """int main(){
#             float i;
#             i = 0.0;
#             for (i;i < 10.0;i = i + 1.0)
#                 if (i == 5) break;
#         }"""
#         expect = "Type Mismatch In Statement: For(Id(i);BinaryOp(<,Id(i),FloatLiteral(10.0));BinaryOp(=,Id(i),BinaryOp(+,Id(i),FloatLiteral(1.0)));If(BinaryOp(==,Id(i),IntLiteral(5)),Break()))"
#         self.assertTrue(TestChecker.test(input,expect,488))

#     def test_random_continuestmt(self):
#         input = """int main(){
#             boolean b;
#             int i, j;
#             j = 10;
#             for (i = 0; i < 10; i = i + 1) {
#                 b = i > 5;
#                 if (b == true) continue;
#             }
#         }"""
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,489))

#     def test_random_returnstmt(self):
#         input = """int main(){
#             float y, i;
#             y = 0;
#             for (i = 0; i < 10; i = i + 1) {
#                 y = y + 1;
#                 if (y > 3) {
#                     y = 0;
#                     break;
#                 }
#             }
#             return y;
#         }"""
#         expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(y),BinaryOp(+,Id(y),IntLiteral(1))),If(BinaryOp(>,Id(y),IntLiteral(3)),Block([BinaryOp(=,Id(y),IntLiteral(0)),Break()]))]))"
#         self.assertTrue(TestChecker.test(input,expect,490))

#     def test_random_funccall(self):
#         input = """int[] ntt(int n[], int t[]){
#             return n[t]+t[n];
#         }
#         int main(){
#             int n[4], t[4];
#             if (ntt(n[3],t[0]) != 0) return ntt(n[3],t[3]);
#         }"""
#         expect = "Type Mismatch In Expression: ArrayCell(Id(n),Id(t))"
#         self.assertTrue(TestChecker.test(input,expect,491))

#     def test_random_expression(self):
#         input = """int main(){
#             boolean a,b,c;
#             int d;
#             a = b && c || d;
#         }"""
#         expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(&&,Id(b),Id(c)),Id(d))"
#         self.assertTrue(TestChecker.test(input,expect,492))

#     def test_random_recursion(self):
#         input = """
#         int foo(int a){
#             return a + foo(--a);
#         }
#         int main(){
#         }"""
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,493))

#     def test_random_recursion_false(self):
#         input = """int ntt(int n, int t){
#             return n+t;
#         }
#         int main(){
#             if (ntt(3,0) != 0) return ntt(3,3);
#             return ntt(3);
#         }"""
#         expect = "Type Mismatch In Expression: CallExpr(Id(ntt),[IntLiteral(3)])"
#         self.assertTrue(TestChecker.test(input,expect,494))

#     def test_random_return_false(self):
#         input = """int main(int args){
#             int x,y,z[3];
#             for(i=5;i>0;--i) x=y;
#             return args;
#         }"""
#         expect = "Undeclared Identifier: i"
#         self.assertTrue(TestChecker.test(input,expect,495))

#     def test_random_ifstmt_false(self):
#         input = """void main(){
#             int a;
#             if (a == 5) a = a + 1.0;
#             else a = a + 0.2;
#         }"""
#         expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.0)))"
#         self.assertTrue(TestChecker.test(input,expect,496))

#     def test_forstmt_ifstmt(self):
#         input = """int main(){
#             int i, j, a[5];
#             for (i = 10; i > 0; --i)
#                 for (j = 0; j < i; j = j + 1)
#                     a[i] = j;
#             a[0] = 0;
#         }"""
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,497))

#     def test_breakstmt_forstmt(self):
#         input = """void main(){
#             int i;
#             i = 0;
#             string s;
#             s = "";
#             for (i;i < 10;i = i + 1)
#                 if (i == 5) break;
#                 else s = s + "t";
#         }"""
#         expect = "Type Mismatch In Expression: BinaryOp(+,Id(s),StringLiteral(t))"
#         self.assertTrue(TestChecker.test(input,expect,498))

#     def test_returnstmt_forstmt_ifstmt(self):
#         input = """int main(){
#             int y, i;
#             y = 0;
#             for (i = 0; i < 10; i = i + 1) {
#                 y = y + 1;
#                 if (y < 3) return y;
#             }
#         }"""
#         expect = "Function main Not Return "
#         self.assertTrue(TestChecker.test(input,expect,499))

# 1712345
# Dang Minh Ngoc
import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
	# ------------------------------------------------------------------------------------------------------
	def test_redeclared_var_in_global_scope(self):
		"test_no_entry_point"
		input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        float scope;"""
		expect = "Redeclared Variable: scope"
		self.assertTrue(TestChecker.test(input, expect, 400))

	def test_redeclared_global_var_in_local_scope(self):
		"test_no_entry_point"
		input = """int global, scope[100];
        void main() {
            int global[10];
            return ;
            // Do nothing in here
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 401))

	def test_redeclared_var_in_local_scope(self):
		input = """int global, scope[100];
        void main() {
            int a,b;
            float x,y,a[10], t;
        }
        """
		expect = "Redeclared Variable: a"
		self.assertTrue(TestChecker.test(input, expect, 402))

	def test_redeclared_var_with_func_name(self):
		input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        float main;"""
		expect = "Redeclared Variable: main"
		self.assertTrue(TestChecker.test(input, expect, 403))

	def test_redeclared_var_in_local_scope_with_func_name(self):
		input = """int global, scope[100];
        void main() {
            boolean main[100];
            int bts, yoongi;
            // Do nothing in here
        }
        float arr[10];"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 404))

	def test_redeclared_func(self):
		input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        int main(float var1, float var_arr[]) {
            var1 = var_arr[0];
            return 1+0-1;
        }"""
		expect = "Redeclared Function: main"
		self.assertTrue(TestChecker.test(input, expect, 405))

	def test_redeclared_func_with_local_var_name(self):
		input = """int global;

        void main() {
            // Do nothing in here
            scope("Born Coder :>");
            {int scope;}
        }
        float scope(string message) {
            putString(message);
            return getFloat();
        }"""
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 406))

	def test_redeclared_func_with_var_name(self):
		input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        float scope(string message) {
            putString(message);
            return getFloat();
        }"""
		expect = "Redeclared Function: scope"
		self.assertTrue(TestChecker.test(input, expect, 407))

	def test_redeclared_param(self):
		input = """int global, scope[100];
        int main(int BTS, string BTS[]) {
           int a;
           a = 10;
           return a; 
        }
        """
		expect = "Redeclared Parameter: BTS"
		self.assertTrue(TestChecker.test(input, expect, 408))

	def test_redeclared_param_with_global_id(self):
		input = """int global, scope[100];
        void main(int global, int main) {
            // Do nothing in here
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 409))

	def test_undeclared_id(self):
		input = """int JIN, SUGA;
        void main(int global, int main) {
            {
                SUGA + JIN > SUGA - JIN;
            }
            RM = "leader";
        }
        """
		expect = "Undeclared Identifier: RM"
		self.assertTrue(TestChecker.test(input, expect, 410))

	def test_undeclared_id2(self):
		input = """string BTS[7];
        void main(int global, int main) {
            global = pow(BTS,7);
        }
        int pow(string idol[], int no){
            putString(idol[7]);
            return no*_well_known;
        }
        """
		expect = "Undeclared Identifier: _well_known"
		self.assertTrue(TestChecker.test(input, expect, 411))

	def test_undeclared_func(self):
		input = """string FourIV;
        int main(int global, int main) {
            putInt(exp);
            global = pow(FourIV,7);
            return global;
        }
        int exp;

        """
		expect = "Undeclared Function: pow"
		self.assertTrue(TestChecker.test(input, expect, 412))

	def test_undeclared_func2(self):
		input = """string FourIV;
        int main(int global, int main) {
            putInt(exp);
            global = (getInt()*7);
            return global;
        }
        int exp;
        void factor(int a, int b) {
            a=b=exp;
            print(a+b);
            return ;
        }

        """
		expect = "Undeclared Function: print"
		self.assertTrue(TestChecker.test(input, expect, 413))

	def test_type_mismatch_stmt_in_if_else(self):
		input = """
        // Global scope here
        string os_greets, str;
        int arr[10];
        int main(int global, int main) {
            putString(os_greets);
            global = exp(arr);
            return global;
        }
        int exp(int array[]){
            //Get value
            int index;
            index = getInt();
            if (index < array[index]) 
                return index;
            else
                return index + array[index];
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 414))

	def test_type_mismatch_stmt_in_if(self):
		input = """
        int main(int global, int main) {
            putString("Hello World");
            exp(130613);
            return global;
        }
        void exp(int i){
            //Get value
            int index;
            index = random[0] = getInt();
            if (getFloat()) 
                return ;
        }
        int random[1]; 
        """
		expect = "Type Mismatch In Statement: If(CallExpr(Id(getFloat),[]),Return())"
		self.assertTrue(TestChecker.test(input, expect, 415))

	def test_type_mismatch_stmt_in_for(self):
		input = """
        int main() {
            int i;
            for (i = 1; i < 11; 1+i)
            {
                putString("%d i");
            }
            return 0;
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 416))


	def test_type_mismatch_stmt_in_for_expr2(self):
		input = """
        int main() {
            int i;
            for (i = 1; ((i)); 1+i)
            {
                putString("%d i");
            }
            return 0;
        }
        """
		expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));Id(i);BinaryOp(+,IntLiteral(1),Id(i));Block([CallExpr(Id(putString),[StringLiteral(%d i)])]))"
		self.assertTrue(TestChecker.test(input, expect, 418))

	def test_type_mismatch_stmt_in_for_expr3(self):
		input = """
        void main() {
            int i;
            for (i = 1; i < 11; "hello world")
            {
                putString("%d i");
            }
        }
        """
		expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(11));StringLiteral(hello world);Block([CallExpr(Id(putString),[StringLiteral(%d i)])]))"
		self.assertTrue(TestChecker.test(input, expect, 419))

	def test_type_mismatch_stmt_in_dowhile(self):
		input = """
        int main()
        {
	        int j;
            j=0;
	        do
	        {
		        printf("Value of variable j is: %d", j);
		        j = j+1;
	        }while (j<=3);
	        return 0;
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 420))

	def test_type_mismatch_stmt_in_dowhile_cond(self):
		input = """
        int main()
        {
	        int j;
            j=0;
	        do
	        {
		        printf("Value of variable j is: %d", j);
		        j = j+1;
	        }while (printf("Error here", 1));
	        return 0;
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
		expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(printf),[StringLiteral(Value of variable j is: %d),Id(j)]),BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)))])],CallExpr(Id(printf),[StringLiteral(Error here),IntLiteral(1)]))"
		self.assertTrue(TestChecker.test(input, expect, 421))

	def test_type_mismatch_stmt_return_void(self):
		input = """
        void main(int argc)
        {
	        return printf("greetings from main", 10);
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 422))

	def test_type_mismatch_stmt_return_nothing(self):
		input = """
        void main(int argc)
        {
            printf("What to do?", argc);
	        return ;
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 423))

	def test_type_mismatch_stmt_return_matching_case(self):
		input = """
        int main(int argc, string argv[])
        {
            argv[0] = printf("What to do?", argc);
	        return 0;
        }
        string printf(string str, int elem) {
            putString(str);
            putInt(elem);
            return ;
        }
        """
		expect = "Type Mismatch In Statement: Return()"
		self.assertTrue(TestChecker.test(input, expect, 424))



	def test_type_mismatch_stmt_return_coerced_case(self):
		input = """
        float base;
        boolean main(int argc, float argv[])
        {
            putFloat(greater(argv, argc));
            return true;
        }
        float greater(float arr[], int idx) {
            if (arr[idx] >= base)
                return idx;
            else
                return -1;            
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 426))

	def test_type_mismatch_stmt_return_coerced_case2(self):
		input = """
        float base;
        boolean main(int argc, float argv[])
        {
            putInt(greater(argv, argc));
            return true;
        }
        int greater(float arr[], int idx) {
            if (arr[idx] >= base)
                return arr[idx];
            else
                return -1;            
        }
        """
		expect = "Type Mismatch In Statement: Return(ArrayCell(Id(arr),Id(idx)))"
		self.assertTrue(TestChecker.test(input, expect, 427))


	def test_type_mismatch_stmt_return_array2(self):
		input = """
        float base;
        float[] main(int argc, int argv[])
        {

            return greater(argv, argc);
        }
        int[] greater(int arr[], int idx) {
            if (arr[idx] >= base)
                return arr;
            else {
                int tmp[10];
                return tmp;  
            }          
        }
        """
		expect = "Type Mismatch In Statement: Return(CallExpr(Id(greater),[Id(argv),Id(argc)]))"
		self.assertTrue(TestChecker.test(input, expect, 429))

	def test_type_mismatch_expr_arr_subscript(self):
		input = """
        int yoongi;
        void main(int argc, int argv[])
        {
            BTS(argv, argc)[0] = yoongi;
        }
        int[] BTS(int arr[], int idx) {
            if (arr[idx] >= yoongi)
                return arr;
            else {
                int tmp[10];
                return tmp;  
            }          
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 430))

	def test_type_mismatch_expr_arr_subscript(self):
		input = """
        int yoongi;
        void main(int argc, int argv[])
        {
            float error_idx;
            error_idx = 0.0;
            {
                BTS(argv, argc)[error_idx] = yoongi;
            }
        }
        int[] BTS(int arr[], int idx) {
            if (arr[idx] >= yoongi)
                return arr;
            else {
                int tmp[10];
                return tmp;  
            }          
        }
        """
		expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(BTS),[Id(argv),Id(argc)]),Id(error_idx))"
		self.assertTrue(TestChecker.test(input, expect, 430))

	def test_type_mismatch_expr_arr_subscript2(self):
		input = """
        int yoongi;
        void main(int argc, int argv[])
        {
            float error_idx;
            error_idx = 0.0;
            {
                BTS(argv, argc)[7] = yoongi;
            }
        }
        int BTS(int arr[], int idx) {
            if (arr[idx] >= yoongi)
                return idx;
            else {
                return -1;  
            }          
        }
        """
		expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(BTS),[Id(argv),Id(argc)]),IntLiteral(7))"
		self.assertTrue(TestChecker.test(input, expect, 431))

	def test_type_mismatch_expr_binary_assign(self):
		input = """
        int global;
        void main(int argc, int argv[])
        {
            int x,y,z;
            boolean t;
            x=y=z=global=1;
            t=true;
            {
                string str;
                str = "Minh Ngoc";
                float f;
                f = 1.5e-09;
            }
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 432))

	def test_type_mismatch_expr_binary_assign2(self):
		input = """
        int global;
        void main(int argc, int argv[])
        {
            int x,y,z;
            float a;
            a = 1;
            x = a;
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),Id(a))"
		self.assertTrue(TestChecker.test(input, expect, 433))

	def test_type_mismatch_expr_binary_assign_lhs_is_func_name(self):
		input = """
        int global;
        string swap(int a, int b) {
            int t;
            t = a;
            a = b; b= t;
            return "Done";
        }
        int main(string argv)
        {
            swap = argv;
            return 0;
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(swap),Id(argv))"
		self.assertTrue(TestChecker.test(input, expect, 434))

	def test_type_mismatch_expr_binary_assign_arr_address_as_operands(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            int main[1];
            {
                arr = main;
            }
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),Id(main))"
		self.assertTrue(TestChecker.test(input, expect, 435))

	def test_type_mismatch_expr_binary_num_op(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            2+5;
            3.5-6e-1;
            2*3.7;
            1/3*7;
            {
                int a,b,c[2];
                float x,y,z[10];
                a = b = 0;
                x = y = .5;
                a*b - 5 +7/5;
                3-a+x*b-c[0];
                z[5] / 4 + 3 * c[1];
            }
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 436))

	def test_type_mismatch_expr_binary_add_string(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            arr[1] + "string";
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),StringLiteral(string))"
		self.assertTrue(TestChecker.test(input, expect, 437))

	def test_type_mismatch_expr_binary_divide_boolean(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = false;
            arr[1] + b;
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),Id(b))"
		self.assertTrue(TestChecker.test(input, expect, 438))

	def test_type_mismatch_expr_binary_mod_float(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            float t;
            t = 0.0;
            arr[1] % (arr[0]/arr[1]*t);
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(%,ArrayCell(Id(arr),IntLiteral(1)),BinaryOp(*,BinaryOp(/,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),Id(t)))"
		self.assertTrue(TestChecker.test(input, expect, 439))

	def test_type_mismatch_expr_binary_logic_op(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = false || true && (1==1) || !(2>=4);
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 440))

	def test_type_mismatch_expr_binary_or_number(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            2 || arr[9];
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(||,IntLiteral(2),ArrayCell(Id(arr),IntLiteral(9)))"
		self.assertTrue(TestChecker.test(input, expect, 441))

	def test_type_mismatch_expr_binary_compare_string(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            arr[0] == "string error";
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(==,ArrayCell(Id(arr),IntLiteral(0)),StringLiteral(string error))"
		self.assertTrue(TestChecker.test(input, expect, 442))

	def test_type_mismatch_expr_binary_and_int(self):
		input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = arr[0] >= 1 || true;
            b && 1;
        }
        """
		expect = "Type Mismatch In Expression: BinaryOp(&&,Id(b),IntLiteral(1))"
		self.assertTrue(TestChecker.test(input, expect, 443))

	def test_type_mismatch_expr_unary(self):
		input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = arr[0] >= 1 || true;
            -b;
        }
        """
		expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
		self.assertTrue(TestChecker.test(input, expect, 444))

	def test_type_mismatch_expr_unary2(self):
		input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = arr[0] >= 1 || true;
            -(2*4.5) < 1 || !"string";
        }
        """
		expect = "Type Mismatch In Expression: UnaryOp(!,StringLiteral(string))"
		self.assertTrue(TestChecker.test(input, expect, 445))

	def test_type_mismatch_func_call(self):
		input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            getInt(arr);
        }
        """
		expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[Id(arr)])"
		self.assertTrue(TestChecker.test(input, expect, 446))

	def test_type_mismatch_func_call2(self):
		input = """
        float arr[10],x,y;
        boolean BTS, TXT;
        void main(int argc, int argv[])
        {
            putString(true);
        }
        """
		expect = "Type Mismatch In Expression: CallExpr(Id(putString),[BooleanLiteral(true)])"
		self.assertTrue(TestChecker.test(input, expect, 447))

	def test_type_mismatch_func_call_passing_array(self):
		input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            test(arr); // OK
            {
                string greets[2];
                test((pointer())); // OK
                test(greets); // Fail
            }
        }
        string yeonjun;
        void test(int arr[]) {
            putInt(arr[0]);
        }

        int[] pointer() {
            int tmp[10];
            return tmp;
        }
        """
		expect = "Type Mismatch In Expression: CallExpr(Id(test),[Id(greets)])"
		self.assertTrue(TestChecker.test(input, expect, 448))

	def test_type_mismatch_func_call_passing_coerced(self):
		input = """
        int arr;
        void main(int argc, int argv[])
        {
            test(arr); // OK
            {
                boolean bool_arr[10];
                test((pointer())); // OK
                test(bool_arr); // Fail
            }
        }

        void test(float arr) {
            putInt(arr);
        }

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
		expect = "Type Mismatch In Expression: CallExpr(Id(test),[Id(bool_arr)])"
		self.assertTrue(TestChecker.test(input, expect, 449))

	def test_type_function_not_return(self):
		input = """
        int arr;
        void main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;
            odd_sum = even_sum = "number";
            float _num;
            _num =10;
            printf("Enter the value of num", "0");

            for (num*num; i <= 13.06e13; num+4)
            {
                if (i % 2 == 0)
                    even_sum = even_sum;
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                }
            }
        printf("Sum of all odd numbers  = %d\\n", odd_sum);
        printf("Sum of all even numbers = %d\\n", even_sum);
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
        }
        """
		expect = "Function pointer Not Return "
		self.assertTrue(TestChecker.test(input, expect, 450))

	def test_type_function_not_return_in_for_loop(self):
		input = """
        int arr;
        int main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;


            printf("Enter the value of num", "0");

            for (num*num; i <= 13.06e13; num+4)
            {
                odd_sum = even_sum = "number";
                float _num;
                _num =10;
                if (i % 2 == 0)
                    even_sum = even_sum;
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                }
                return num;
            }
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
		expect = "Function main Not Return "
		self.assertTrue(TestChecker.test(input, expect, 451))

	def test_type_function_not_return_in_one_branch_of_loop(self):
		input = """
        int arr;
        int main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;
            odd_sum = even_sum = "number";
            float _num;
            _num =10;
            printf("Enter the value of num", "0");

            {
                if (i % 2 == 0)
                    even_sum = even_sum;
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                    return 0;
                }
            }
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
            } 
        

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
		expect = "Function main Not Return "
		self.assertTrue(TestChecker.test(input, expect, 452))

	def test_type_function_not_return_do_while(self):
		input = """
        int arr;
        int main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;
            odd_sum = even_sum = "number";
            float _num;
            _num =10;

            do
                printf("Enter the value of num", "0");
                if (i % 2 == 0)
                    {even_sum = even_sum; return 1;}
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                    return 0;
                }
            while(false);
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 453))

	def test_type_function_not_return_block(self):
		input = """
        int i,j,k[100];
        int main()
        {
            do
                printf("Enter the value of num", "0");
                if (i % 2 == 0) {
                    for(i;994 == 234;i) 
                        break;
                    return 4499;
                }
                else {
                    float t;
                    t = 0.4499;

                    return 0;
                }
            while(false);
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
            {return tmp;}
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 454))

	def test_break_not_in_loop(self):
		input = """
        string arr[2];
        string[] main()
        {
            printf("Input desired number", arr[0]);
            factorial(num);
            return arr;
        }

        void printf(string str, string num) {
            putString(str);
            num = "input nunmber";
        }
        int num;
        int factorial(int n) {
            if (n <= 1)
                return 1;
            else {
                break;
                return n*factorial(n-1);  
            }           
        }
        """
		expect = "Break Not In Loop"
		self.assertTrue(TestChecker.test(input, expect, 455))

	def test_continue_not_in_loop(self):
		input = """
        int check_armstrong(int n) {
            int sum, temp;
            int remainder,digits; 
            digits = 0;

            temp = n;

            do
                digits;
                temp = temp/10;
            while (temp != 0);

            temp = n;
            do remainder = temp%10;
                sum = sum + power(remainder, digits)[4*temp-1];
                temp = temp/10;
                break;
            while (temp != 0);

            {continue;} // error here


            if (n == sum)
                return 1;
            else
                return 0;
        }
        void main() {
            check_armstrong(9);
        }

        int[]  power(int n, int r) {
            int BTS, Yoongi[3];
            Yoongi[2] = 1;
            int c,p;
            p=10;
            for (c = 1; c <= r; c+1)
                if(true) 
                    continue;
                else
                    p=p*n;

            return Yoongi;  
        }
        """
		expect = "Continue Not In Loop"
		self.assertTrue(TestChecker.test(input, expect, 456))

	def test_no_entry_point(self):
		input = """
        int swap()
        {
            int x, y, t;
            x = 13;
            y = 00000000000000000000000000000000004;
            t = 0;

            ("Enter two integers\\n");
            "Before Swapping\\nFirst integer = %d\\nSecond integer = %d\\n"; (x* y);

            t = x;
            x = y;
            y = t;
            "After Swapping\\nFirst integer = %d\\nSecond integer = %d\\n"; (x- y) < 49 || !(-(x+y)/3 < 6e25);

            return 0;
        }
        """
		expect = "No Entry Point"
		self.assertTrue(TestChecker.test(input, expect, 457))

	def test_no_entry_point2(self):
		input = """
        void swap(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,2);
        }

        void printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            swap(0,999);
        }
        """
		expect = "No Entry Point"
		self.assertTrue(TestChecker.test(input, expect, 458))

	def test_unreachable_func(self):
		input = """
        int[] foo() {
            int arr[10];
            return arr;
        }
        void main(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,2);
        }

        void printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            main(0,999);
        }
        """
		expect = "Unreachable Function: foo"
		self.assertTrue(TestChecker.test(input, expect, 459))


	def test_not_left_value_literal(self):
		input = """
        void swap(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,2);
        }

        float global;
        void main(int n)
        {
            swap(1,2);
            int c, result;
            result = 1;

            for (c = 1; c <= n; c+1)
                100 = result*c;

            return ;
        }

        void printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            printRes(0.e25,999,3);
        }
        """
		expect = "Not Left Value: IntLiteral(100)"
		self.assertTrue(TestChecker.test(input, expect, 461))

	def test_not_left_value_func(self):
		input = """

        float global;
        void main(int n)
        {
            int c, result;
            result = 1;
            printRes(0.5,4.97e01, 4) = 1==1 || true && false;
            for (c = 1; c <= n; c+1)
                result = result*c;

            return ;
        }

        boolean printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            printRes(0.e25,999,3);
            return true;
        }
        """
		expect = "Not Left Value: CallExpr(Id(printRes),[FloatLiteral(0.5),FloatLiteral(49.7),IntLiteral(4)])"
		self.assertTrue(TestChecker.test(input, expect, 462))

	def test_not_left_value_func_return_array(self):
		input = """
        void swap(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,test)[9] = !true || (25*x<=0.5-y); 
        }
        boolean test[2];
        float global;
        void main(int n)
        {
            int c, result;
            result = 1;
            string t;
            t = "string here";
            for (c = 1; c <= n; c+1)
            {
                result = result*c;
                swap(c, result);
            }

            return ;
        }

        boolean[] printRes(float var1, float var2, boolean num[]) {
            putFloat(var1);
            putFloat(var2);
            printRes(0.e25,999,test);

            return num;
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 463))

	def test_not_left_value_expr(self):
		input = """
        float flag[10];
        string CTF;
        int main() {
            flag[2] = flag[0]*5 / 59;
            true && !(9 > 4)  = flag[8];
            return 0;
        }
        """
		expect = "Not Left Value: BinaryOp(&&,BooleanLiteral(true),UnaryOp(!,BinaryOp(>,IntLiteral(9),IntLiteral(4))))"
		self.assertTrue(TestChecker.test(input, expect, 464))

	def test_pure_vardecl(self):
		input = """
        int a,x,b,XXX, YYY, __[99],d;
        float ate[000], youtube;
        boolean facebool, twitter[2], yahoo_yayayayay;
        string _name_, _id_;
        string JLPT, _____[1999];
        """
		expect = "No Entry Point"
		self.assertTrue(TestChecker.test(input, expect, 480))

	def test_pure_funcdecl(self):
		input = """
        void foo() {
            // do this, so that
        }

        int[] random_num_list(int a, int b) {
            int lst[2];
            lst[0] = a;
            lst[1] = a - b;
            return lst;
        }

        boolean main() {
            foo();
            return redundance(random_num_list(44,99));
        }

        boolean redundance(int list[]) {
            if (list[0] != 0)
                return true;
            else
                return !(list[0] <= list[1]);
        } 
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 481))

	def test_pure_funcdecl_with_error_in_return(self):
		input = """
        void foo() {
            // do this, so that
        }

        int[] random_num_list(int a, int b) {
            int lst[2];
            lst[0] = a;
            lst[1] = a - b;
            return lst;
        }

        boolean main() {
            foo();
            return redundance(random_num_list(44,99)); // Error here
        }

        int redundance(int list[]) {
            if (list[0] != 0)
                return 0;
            else
                return -(list[0]-list[1]);
        } 
        """
		expect = "Type Mismatch In Statement: Return(CallExpr(Id(redundance),[CallExpr(Id(random_num_list),[IntLiteral(44),IntLiteral(99)])]))"
		self.assertTrue(TestChecker.test(input, expect, 482))

	def test_no_error_program(self):
		input = """
        int i;
        int f() {
            return 200;
        }
        void main() {
            int main;
            main = f();
            putIntLn(main);
            {
                int i;
                int main;
                int f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 483))



	def test_error_use_var_ass_func(self):
		input = """
        void main( int a[], int var )
        {
            int k, i, l, j;
            i=j=99;
            k=l=i-9*j;

            for ( k = 0;k < var;k() )   //error here
            {
                for ( i = 0;i <= var;i )
                {
                    l = (a[ i ])-a[ k ];

                    for ( j = 0;j <= var;j )
                    {
                        if ( i != k )
                            a[j] = a[a[k]*a[j]-(l*a[k])];
                    }
                }
            }
        }
        """
		expect = "Type Mismatch In Expression: CallExpr(Id(k),[])"
		self.assertTrue(TestChecker.test(input, expect, 485))

	def test_type_mismatch_in_dowhile(self):
		input = """
        string a,b,x,__;
        int main(string argv[], int argc) { do do {} while(__); while(true); }
        int minDistance(int dist[], int sptSet[]) { 
            if (_) return dist[0];
        } 
        float b1, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean _b, c2, X0XX, YY8Y, _3__[343434343], h6cmut, ed2u;
        """
		expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(__))"
		self.assertTrue(TestChecker.test(input, expect, 487))

	def test_undeclared_func_in_dowhile(self):
		input = """
        string a,b,x,__;
        int main(string argv[], int argc) { do do {} while(isDone(__)); while(true); }
        int minDistance(int dist[], int sptSet[]) { 
            if (_) return dist[0];
        } 
        float b1, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean _b, c2, X0XX, YY8Y, _3__[343434343], h6cmut, ed2u;
        """
		expect = "Undeclared Function: isDone"
		self.assertTrue(TestChecker.test(input, expect, 488))

	def test_many_if_else(self):
		input = """
        void main(int a[], int m, int b[], int n, int sorted[]) {
            int i, j, k;
            j = k = 0;

            for (i = 0;check(true);m+n) {
                if (j < m && k < n) {
                    if (a[j] < b[k]) {
                        sorted[i] = a[j];
                        j + 1;
                    }
                    else {
                        sorted[i] = b[k];
                        k+2;
                    }
                    i+0;
                }
                else if (j == m) {
                    for (i; i < m + n;(a[9])) {
                        sorted[i] = b[k];
                    }
                    continue;
                }
                else {
                    for (m; i < m + n;a[2*5-m+0]) {
                        sorted[i] = a[j];
                        break;
                    }
                }
            }
        }
        boolean check(boolean t) {
            return t;
        }
        """
		expect = ""
		self.assertTrue(TestChecker.test(input, expect, 489))

	def test_undeclared_var_in_dowhile(self):
		input = """
        string a,b,x,__;
        int main(string argv[], int argc) { do do {} while(_b); a = greets_from_os; while(true); }
        int minDistance(int dist[], int sptSet[]) { 
            if (_) return dist[0];
        } 
        float b1, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean _b, c2, X0XX, YY8Y, _3__[343434343], h6cmut, ed2u;
        """
		expect = "Undeclared Identifier: greets_from_os"
		self.assertTrue(TestChecker.test(input, expect, 490))

	def test_not_left_value_expr_in_dowhile(self):
		input = """
        string Exp, Mana, mana[0]; 
        int Array[10], PPL_test[100];
        int main(string argv[], int argc) { 
            string tmp[2];
            PPL(tmp);
            if (PPL_test[4] > 0)
                return Array[007]*0;
            return 0;
        }
        string[] PPL(string s[]) {
            do 
                PPL_test[10] + Array[PPL_test[0]] = "Go go go!!!"; // error here
            while (CSE[1]);
            return mana;
        }
        boolean HCMUT, CSE[2], VNU;
        string FourIV;
        float _01,Finish,_;

        """
		expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(PPL_test),IntLiteral(10)),ArrayCell(Id(Array),ArrayCell(Id(PPL_test),IntLiteral(0))))"
		self.assertTrue(TestChecker.test(input, expect, 494))

	def test_type_mismatch_in_return_stmt(self):
		input = """
        string Exp, Mana, mana[1]; 
        int Array[10], PPL_test[100];
        int main(string argv[], int argc) { 
            string tmp[2];
            PPL(tmp);
            if (PPL_test[4] > 0)
                return Array[007]*0;
            return 0;
        }
        string[] PPL(string s[]) {
            do 
                mana[Array[PPL_test[0]]] = "Go go go!!!"; 
            while (CSE[1]);
            return Mana;    // Error here
        }
        boolean HCMUT, CSE[2], VNU;
        string FourIV;
        float _01,Finish,_;

        """
		expect = "Type Mismatch In Statement: Return(Id(Mana))"
		self.assertTrue(TestChecker.test(input, expect, 495))

	def test_unreachable_function2(self):
		input = """
        int main(string argv[], int argc) { return 0;  }
        float solve_for_y(float a, float b, float c)
        {
            float Y;
            if(a <= 0) {
                putStringLn("Value of Y cannot be predicted");
            }
            else {
                Y = -(b + c) / a;
            }
            return Y;
        }
        """
		expect = "Unreachable Function: solve_for_y"
		self.assertTrue(TestChecker.test(input, expect, 496))

	def test_unreachable_function_self_called(self):
		input = """
        int compare_strings(string a[], string b[])
        {
            int c; c = 0;
            int _a[2], _b[9];
            do {}
                if (_a[c] == 0 || _b[c] < 0)
                {
                    for(c;c==0;c) {
                        compare_strings(a,b);
                    }
                    break;
                }
            while (_a[c] == _b[c]);           

            if (_a[c] == 404 && _b[c] == c)
                return 0;
            else
                return -1;
        }
        void main() {}
        """
		expect = "Unreachable Function: compare_strings"
		self.assertTrue(TestChecker.test(input, expect, 497))
