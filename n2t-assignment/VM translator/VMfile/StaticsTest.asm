@256
D = A
@SP
M = D
@1500
D = A
@LCL
M = D
@1600
D = A
@ARG
M = D
@1700
D = A
@THIS
M = D
@1800
D = A
@THAT
M = D
//Call Sys.init 0
@StaticsTest.0$ret.1
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
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@StaticsTest.Sys.init
0;JMP
(StaticsTest.0$ret.1)
//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/08/FunctionCalls/StaticsTest/Class1.vm
//
//// Stores two supplied arguments in static[0] and static[1].
//function Class1.set 0
(StaticsTest.Class1.set)
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
//pop static 0
@SP
M = M-1
A = M
D = M
@StaticsTest.0
M = D
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
//pop static 1
@SP
M = M-1
A = M
D = M
@StaticsTest.1
M = D
//push constant 0
@0
D = A
@SP
M = M+1
A = M-1
M = D
//return
@LCL
D = M
@endFrame
M = D
@5
D = A
@endFrame
A = M-D
D = M
@retAddr
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
@endFrame
A = M-1
D = M
@THAT
M = D
@2
D = A
@endFrame
A = M-D
D = M
@THIS
M = D
@3
D = A
@endFrame
A = M-D
D = M
@ARG
M = D
@4
D = A
@endFrame
A = M-D
D = M
@LCL
M = D
@retAddr
A = M
0;JMP
//
//// Returns static[0] - static[1].
//function Class1.get 0
(StaticsTest.Class1.get)
//push static 0
@StaticsTest.0
D = M
@SP
M = M+1
A = M-1
M = D
//push static 1
@StaticsTest.1
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
@endFrame
M = D
@5
D = A
@endFrame
A = M-D
D = M
@retAddr
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
@endFrame
A = M-1
D = M
@THAT
M = D
@2
D = A
@endFrame
A = M-D
D = M
@THIS
M = D
@3
D = A
@endFrame
A = M-D
D = M
@ARG
M = D
@4
D = A
@endFrame
A = M-D
D = M
@LCL
M = D
@retAddr
A = M
0;JMP
//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/08/FunctionCalls/StaticsTest/Class2.vm
//
//// Stores two supplied arguments in static[0] and static[1].
//function Class2.set 0
(StaticsTest.Class2.set)
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
//pop static 0
@SP
M = M-1
A = M
D = M
@StaticsTest.0
M = D
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
//pop static 1
@SP
M = M-1
A = M
D = M
@StaticsTest.1
M = D
//push constant 0
@0
D = A
@SP
M = M+1
A = M-1
M = D
//return
@LCL
D = M
@endFrame
M = D
@5
D = A
@endFrame
A = M-D
D = M
@retAddr
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
@endFrame
A = M-1
D = M
@THAT
M = D
@2
D = A
@endFrame
A = M-D
D = M
@THIS
M = D
@3
D = A
@endFrame
A = M-D
D = M
@ARG
M = D
@4
D = A
@endFrame
A = M-D
D = M
@LCL
M = D
@retAddr
A = M
0;JMP
//
//// Returns static[0] - static[1].
//function Class2.get 0
(StaticsTest.Class2.get)
//push static 0
@StaticsTest.0
D = M
@SP
M = M+1
A = M-1
M = D
//push static 1
@StaticsTest.1
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
@endFrame
M = D
@5
D = A
@endFrame
A = M-D
D = M
@retAddr
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
@endFrame
A = M-1
D = M
@THAT
M = D
@2
D = A
@endFrame
A = M-D
D = M
@THIS
M = D
@3
D = A
@endFrame
A = M-D
D = M
@ARG
M = D
@4
D = A
@endFrame
A = M-D
D = M
@LCL
M = D
@retAddr
A = M
0;JMP
//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/08/FunctionCalls/StaticsTest/Sys.vm
//
//// Tests that different functions, stored in two different 
//// class files, manipulate the static segment correctly. 
//function Sys.init 0
(StaticsTest.Sys.init)
//push constant 6
@6
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
//call Class1.set 2
@StaticsTest.Sys.init$ret.2
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
@2
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@StaticsTest.Class1.set
0;JMP
(StaticsTest.Sys.init$ret.2)
//pop temp 0 // Dumps the return value
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
//push constant 23
@23
D = A
@SP
M = M+1
A = M-1
M = D
//push constant 15
@15
D = A
@SP
M = M+1
A = M-1
M = D
//call Class2.set 2
@StaticsTest.Sys.init$ret.3
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
@2
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@StaticsTest.Class2.set
0;JMP
(StaticsTest.Sys.init$ret.3)
//pop temp 0 // Dumps the return value
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
//call Class1.get 0
@StaticsTest.Sys.init$ret.4
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
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@StaticsTest.Class1.get
0;JMP
(StaticsTest.Sys.init$ret.4)
//call Class2.get 0
@StaticsTest.Sys.init$ret.5
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
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@StaticsTest.Class2.get
0;JMP
(StaticsTest.Sys.init$ret.5)
//label WHILE
(StaticsTest.Sys.init$WHILE)
//goto WHILE
@StaticsTest.Sys.init$WHILE
0;JMP
(end)
@end
0;JMP
