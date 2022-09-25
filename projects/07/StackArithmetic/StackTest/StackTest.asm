//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/07/StackArithmetic/StackTest/StackTest.vm
//
//// Executes a sequence of arithmetic and logical operations
//// on the stack. 
//push constant 17
@17
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 17
@17
D = A
@SP
M = M+1
A = M-1
M = D
//eq
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@eq9
D;JEQ
@SP
A = M-1
M = 0
@continue9
0;JMP
(eq9)
@SP
A = M-1
M = 1
(continue9)
//push constant 17
@17
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 16
@16
D = A
@SP
M = M+1
A = M-1
M = D
//eq
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@eq12
D;JEQ
@SP
A = M-1
M = 0
@continue12
0;JMP
(eq12)
@SP
A = M-1
M = 1
(continue12)
//push constant 16
@16
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 17
@17
D = A
@SP
M = M+1
A = M-1
M = D
//eq
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@eq15
D;JEQ
@SP
A = M-1
M = 0
@continue15
0;JMP
(eq15)
@SP
A = M-1
M = 1
(continue15)
//push constant 892
@892
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 891
@891
D = A
@SP
M = M+1
A = M-1
M = D
//lt
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@lt18
D;JLT
@SP
A = M-1
M = 0
@continue18
0;JMP
(lt18)
@SP
A = M-1
M = 1
(continue18)
//push constant 891
@891
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 892
@892
D = A
@SP
M = M+1
A = M-1
M = D
//lt
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@lt21
D;JLT
@SP
A = M-1
M = 0
@continue21
0;JMP
(lt21)
@SP
A = M-1
M = 1
(continue21)
//push constant 891
@891
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 891
@891
D = A
@SP
M = M+1
A = M-1
M = D
//lt
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@lt24
D;JLT
@SP
A = M-1
M = 0
@continue24
0;JMP
(lt24)
@SP
A = M-1
M = 1
(continue24)
//push constant 32767
@32767
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 32766
@32766
D = A
@SP
M = M+1
A = M-1
M = D
//gt
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@gt27
D;JGT
@SP
A = M-1
M = 0
@continue27
0;JMP
(gt27)
@SP
A = M-1
M = 1
(continue27)
//push constant 32766
@32766
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 32767
@32767
D = A
@SP
M = M+1
A = M-1
M = D
//gt
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@gt30
D;JGT
@SP
A = M-1
M = 0
@continue30
0;JMP
(gt30)
@SP
A = M-1
M = 1
(continue30)
//push constant 32766
@32766
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 32766
@32766
D = A
@SP
M = M+1
A = M-1
M = D
//gt
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@gt33
D;JGT
@SP
A = M-1
M = 0
@continue33
0;JMP
(gt33)
@SP
A = M-1
M = 1
(continue33)
//push constant 57
@57
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 31
@31
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 53
@53
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
//push constant 112
@112
D = A
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
//neg
@SP
A = M-1
M = -M
//and
@SP
M = M-1
A = M
D = M
A = A-1
M = M&D
//push constant 82
@82
D = A
@SP
M = M+1
A = M-1
M = D
//or
@SP
M = M-1
A = M
D = M
A = A-1
M = M|D
//not
@SP
A = M-1
M = !M
(end)
@end
0;JMP
