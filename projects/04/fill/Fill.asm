// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
//pseudocode
//
//start = SCREEN
//n = 8192
//i = 0
//
//LOOP:
//  if(KBD != 0) goto WHITE     
//  else goto BLACK
//  goto LOOP
//
//WHITE:
//  i = 0  //SCREEN = 0;
//SET_WHITE
//  if i=n goto LOOP
//  RAM[start+i] = 0
//  i = i + 1
//  goto SET_WHITE
//
//BLACK:
//  i = 0//SCREEN = -1;
//SET_BLACK
//  if i = n goto LOOP
//  RAM[start+i] = -1
//  i = i + 1
//  goto LOOP
//
//256*32=8192个寄存器
//for(i=0, i<8192, i++):
//    M = -1

@SCREEN
D = A
@START
M = D
@8192
D = A
@n
M = D
@i
M = 0
(LOOP)
    @KBD
    D = M
    @WHITE
    D;JEQ
    @BLACK
    D;JNE
    @LOOP
    0;JMP
(WHITE)
    @i
    M = 0
(SET_WHITE)
    @i
    D = M
    @n
    D = D - M
    @LOOP
    D;JEQ
    @START
    D = M
    @i
    A = D + M
    M = 0
    @i
    M = M + 1
    @SET_WHITE
    0;JMP
(BLACK)
    @i
    M = 0
(SET_BLACK)
    @i
    D = M
    @n
    D = D - M
    @LOOP
    D;JEQ
    @START
    D = M
    @i
    A = D + M
    M = -1
    @i
    M = M + 1
    @SET_BLACK
    0;JMP

    