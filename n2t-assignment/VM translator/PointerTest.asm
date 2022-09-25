//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/07/MemoryAccess/PointerTest/PointerTest.vm
//
//// Executes pop and push commands using the 
//// pointer, this, and that segments.
//push constant 3030
@3030
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
//push constant 3040
@3040
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
//push constant 32
@32
D = A
@SP
M = M+1
A = M-1
M = D
//pop this 2
@2
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
@2
D = A
@THIS
M = M - D
//push constant 46
@46
D = A
@SP
M = M+1
A = M-1
M = D
//pop that 6
@6
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
@6
D = A
@THAT
M = M - D
//push pointer 0
@THIS
D = M
@SP
M = M+1
A = M-1
M = D
//push pointer 1
@THAT
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
//push this 2
@2
D = A
@THIS
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
//push that 6
@6
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
(end)
@end
0;JMP
