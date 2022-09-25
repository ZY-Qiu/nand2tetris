//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm
//
//// Performs a simple calculation and returns the result.
//function SimpleFunction.test 2
(SimpleFunction.test)
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
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//not
@SP
A = M-1
M = !M
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
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//push argument 1
@1
D = A
@ARG
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//sub
@SP
M = M-1
A = M
D = M
A = A-1
M = M-D
//return
@LCL
D = M
@endFrame.0
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
@endFrame.0
A = M-1
D = M
@THAT
M = D
@2
D = A
@endFrame.0
A = M-D
D = M
@THIS
M = D
@3
D = A
@endFrame.0
A = M-D
D = M
@ARG
M = D
@4
D = A
@endFrame.0
A = M-D
D = M
@LCL
M = D
@5
D = A
@endFrame.0
A = M-D
A = M
0;JMP
