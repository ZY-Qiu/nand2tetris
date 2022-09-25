//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm
//
//// Pushes and adds two constants.
//push constant 7
@7
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 8
@8
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
(end)
@end
0;JMP
