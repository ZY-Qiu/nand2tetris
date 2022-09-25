@256
D = A
@SP
M = D
//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/08/ProgramFlow/BasicLoop/BasicLoop.vm
//
//// Computes the sum 1 + 2 + ... + argument[0] and pushes the 
//// result onto the stack. Argument[0] is initialized by the test 
//// script before this code starts running.
//push constant 0    
@0
D = A
@SP
M = M+1
A = M-1
M = D
//pop local 0         // initializes sum = 0
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
//label LOOP_START
(LOOP_START)
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
//add
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
//pop local 0	        // sum = sum + counter
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
//push constant 1
@1
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
//pop argument 0      // counter--
@0
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
@0
D = A
@ARG
M = M - D
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
//if-goto LOOP_START  // If counter > 0, goto LOOP_START
@SP
M = M-1
A = M
D = M
@LOOP_START
D;JNE
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
(end)
@end
0;JMP
