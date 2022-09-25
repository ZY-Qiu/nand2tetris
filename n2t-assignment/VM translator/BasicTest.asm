//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/07/MemoryAccess/BasicTest/BasicTest.vm
//
//// Executes pop and push commands using the virtual memory segments.
//push constant 10
@10
D = A
@SP
M = M+1
A = M-1
M = D
//pop local 0
@0
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
@0
D = A
@LCL
M = M - D
//push constant 21
@21
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 22
@22
D = A
@SP
M = M+1
A = M-1
M = D
//pop argument 2
@2
D = A
@ARG
M = M + D
@SP
M = M-1
A = M
D = M
@ARG
A = M
M = D
@2
D = A
@ARG
M = M - D
//pop argument 1
@1
D = A
@ARG
M = M + D
@SP
M = M-1
A = M
D = M
@ARG
A = M
M = D
@1
D = A
@ARG
M = M - D
//push constant 36
@36
D = A
@SP
M = M+1
A = M-1
M = D
//pop this 6
@6
D = A
@THIS
M = M + D
@SP
M = M-1
A = M
D = M
@THIS
A = M
M = D
@6
D = A
@THIS
M = M - D
//push constant 42
@42
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 45
@45
D = A
@SP
M = M+1
A = M-1
M = D
//pop that 5
@5
D = A
@THAT
M = M + D
@SP
M = M-1
A = M
D = M
@THAT
A = M
M = D
@5
D = A
@THAT
M = M - D
//pop that 2
@2
D = A
@THAT
M = M + D
@SP
M = M-1
A = M
D = M
@THAT
A = M
M = D
@2
D = A
@THAT
M = M - D
//push constant 510
@510
D = A
@SP
M = M+1
A = M-1
M = D
//pop temp 6
@5
D = A
@TEMP
M = D
@6
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
//push that 5
@5
D = A
@THAT
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
//push this 6
@6
D = A
@THIS
D = M + D
A = D
D = M
@SP
M = M+1
A = M-1
M = D
//push this 6
@6
D = A
@THIS
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
//sub
@SP
M = M-1
A = M
D = M
A = A-1
M = M-D
//push temp 6
@6
D = A
@5
A = A + D
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
(end)
@end
0;JMP
