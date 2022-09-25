//// Sys.vm for NestedCall test.
//
//// Sys.init()
////
//// Calls Sys.main() and stores return value in temp 1.
//// Does not return.  (Enters infinite loop.)
//
//function Sys.init 0
(Sys.init)
//push constant 4000	// test THIS and THAT context save
@4000
D = A
@SP
M = M+1
A = M-1
M = D
//pop pointer 0
@SP
M = M-1
A = M
D = M
@THIS
M = D
//push constant 5000
@5000
D = A
@SP
M = M+1
A = M-1
M = D
//pop pointer 1
@SP
M = M-1
A = M
D = M
@THAT
M = D
//call Sys.main 0
@1
D = A
@SP
M = M+1
A = M-1
M = D
@LCL
D = M
@SP
M = M+1
A = M-1
M = D
@ARG
D = M
@SP
M = M+1
A = M-1
M = D
@THIS
D = M
@SP
M = M+1
A = M-1
M = D
@THAT
D = M
@SP
M = M+1
A = M-1
M = D
@5
D = A
@0
D = M + D
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@Sys.main
0;JMP
(Sys.Sys.main$ret.1)
//pop temp 1
@5
D = A
@TEMP
M = D
@1
D = A
@TEMP
M = M + D
@SP
M = M-1
A = M
D = M
@TEMP
A = M
M = D
//label LOOP
(Sys.Sys.main$LOOP.1)
//goto LOOP
@Sys.Sys.main$LOOP.1
0;JMP
//
//// Sys.main()
////
//// Sets locals 1, 2 and 3, leaving locals 0 and 4 unchanged to test
//// default local initialization to 0.  (RAM set to -1 by test setup.)
//// Calls Sys.add12(123) and stores return value (135) in temp 0.
//// Returns local 0 + local 1 + local 2 + local 3 + local 4 (456) to confirm
//// that locals were not mangled by function call.
//
//function Sys.main 5
(Sys.main)
@0
D = A
@SP
M = M+1
A = M-1
M = D
@0
D = A
@SP
M = M+1
A = M-1
M = D
@0
D = A
@SP
M = M+1
A = M-1
M = D
@0
D = A
@SP
M = M+1
A = M-1
M = D
@0
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 4001
@4001
D = A
@SP
M = M+1
A = M-1
M = D
//pop pointer 0
@SP
M = M-1
A = M
D = M
@THIS
M = D
//push constant 5001
@5001
D = A
@SP
M = M+1
A = M-1
M = D
//pop pointer 1
@SP
M = M-1
A = M
D = M
@THAT
M = D
//push constant 200
@200
D = A
@SP
M = M+1
A = M-1
M = D
//pop local 1
@1
D = A
@LCL
M = M + D
@SP
M = M-1
A = M
D = M
@LCL
A = M
M = D
@1
D = A
@LCL
M = M - D
//push constant 40
@40
D = A
@SP
M = M+1
A = M-1
M = D
//pop local 2
@2
D = A
@LCL
M = M + D
@SP
M = M-1
A = M
D = M
@LCL
A = M
M = D
@2
D = A
@LCL
M = M - D
//push constant 6
@6
D = A
@SP
M = M+1
A = M-1
M = D
//pop local 3
@3
D = A
@LCL
M = M + D
@SP
M = M-1
A = M
D = M
@LCL
A = M
M = D
@3
D = A
@LCL
M = M - D
//push constant 123
@123
D = A
@SP
M = M+1
A = M-1
M = D
//call Sys.add12 1
@2
D = A
@SP
M = M+1
A = M-1
M = D
@LCL
D = M
@SP
M = M+1
A = M-1
M = D
@ARG
D = M
@SP
M = M+1
A = M-1
M = D
@THIS
D = M
@SP
M = M+1
A = M-1
M = D
@THAT
D = M
@SP
M = M+1
A = M-1
M = D
@5
D = A
@1
D = M + D
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@Sys.add12
0;JMP
(Sys.Sys.add12$ret.2)
//pop temp 0
@5
D = A
@TEMP
M = D
@0
D = A
@TEMP
M = M + D
@SP
M = M-1
A = M
D = M
@TEMP
A = M
M = D
//push local 0
@0
D = A
@LCL
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//push local 1
@1
D = A
@LCL
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//push local 2
@2
D = A
@LCL
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//push local 3
@3
D = A
@LCL
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//push local 4
@4
D = A
@LCL
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//return
@LCL
D = M
@endFrame.2
M = D
@SP
M = M-1
A = M
D = M
@ARG
A = M
M = D
@ARG
D = M+1
@SP
M = D
@endFrame.2
A = M-1
D = M
@THAT
M = D
@2
D = A
@endFrame.2
A = M-D
D = M
@THIS
M = D
@3
D = A
@endFrame.2
A = M-D
D = M
@ARG
M = D
@4
D = A
@endFrame.2
A = M-D
D = M
@LCL
M = D
@Sys.Sys.add12$ret.2
0;JMP
//
//// Sys.add12(int n)
////
//// Returns n+12.
//
//function Sys.add12 0
(Sys.add12)
//push constant 4002
@4002
D = A
@SP
M = M+1
A = M-1
M = D
//pop pointer 0
@SP
M = M-1
A = M
D = M
@THIS
M = D
//push constant 5002
@5002
D = A
@SP
M = M+1
A = M-1
M = D
//pop pointer 1
@SP
M = M-1
A = M
D = M
@THAT
M = D
//push argument 0
@0
D = A
@ARG
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//push constant 12
@12
D = A
@SP
M = M+1
A = M-1
M = D
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//return
@LCL
D = M
@endFrame.2
M = D
@SP
M = M-1
A = M
D = M
@ARG
A = M
M = D
@ARG
D = M+1
@SP
M = D
@endFrame.2
A = M-1
D = M
@THAT
M = D
@2
D = A
@endFrame.2
A = M-D
D = M
@THIS
M = D
@3
D = A
@endFrame.2
A = M-D
D = M
@ARG
M = D
@4
D = A
@endFrame.2
A = M-D
D = M
@LCL
M = D
@Sys.Sys.add12$ret.2
0;JMP
