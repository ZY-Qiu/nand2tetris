// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
//pseudocode
//i=0;
//n=R1;
//R2=0;
//LOOP:
//  if i=n goto END
//  R2 = R2 + R0
//  i = i + 1
//  goto LOOP
//
//END:
//  goto END


    @i
    M = 0
    @R1
    D = M
    @n
    M = D
    @R2
    M = 0
(LOOP)
    @i
    D = M
    @n
    D = D - M
    @END
    D;JEQ
    @R0
    D = M
    @R2
    M = M + D
    @i
    M = M + 1
    @LOOP
    0;JMP
(END)
    @END
    0;JMP