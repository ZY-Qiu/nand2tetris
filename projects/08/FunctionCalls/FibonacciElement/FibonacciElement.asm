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
@FibonacciElement.0$ret.1
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
@FibonacciElement.Sys.init
0;JMP
(FibonacciElement.0$ret.1)
//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/08/FunctionCalls/FibonacciElement/Main.vm
//
//// Computes the n'th element of the Fibonacci series, recursively.
//// n is given in argument[0].  Called by the Sys.init function 
//// (part of the Sys.vm file), which also pushes the argument[0] 
//// parameter before this code starts running.
//
//function Main.fibonacci 0
(FibonacciElement.Main.fibonacci)
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
//push constant 2
@2
D = A
@SP
M = M+1
A = M-1
M = D
//lt                     // checks if n<2
@SP
M = M-1
A = M
D = M
A = A-1
D = M-D
@lt13
D;JLT
@SP
A = M-1
M = 0
@continue13
0;JMP
(lt13)
@SP
A = M-1
M = 1
(continue13)
//if-goto IF_TRUE
@SP
M = M-1
A = M
D = M
@FibonacciElement.Main.fibonacci$IF_TRUE
D;JNE
//goto IF_FALSE
@FibonacciElement.Main.fibonacci$IF_FALSE
0;JMP
//label IF_TRUE          // if n<2, return n
(FibonacciElement.Main.fibonacci$IF_TRUE)
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
//label IF_FALSE         // if n>=2, returns fib(n-2)+fib(n-1)
(FibonacciElement.Main.fibonacci$IF_FALSE)
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
//push constant 2
@2
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
//call Main.fibonacci 1  // computes fib(n-2)
@FibonacciElement.Main.fibonacci$ret.2
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
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@FibonacciElement.Main.fibonacci
0;JMP
(FibonacciElement.Main.fibonacci$ret.2)
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
//call Main.fibonacci 1  // computes fib(n-1)
@FibonacciElement.Main.fibonacci$ret.3
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
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@FibonacciElement.Main.fibonacci
0;JMP
(FibonacciElement.Main.fibonacci$ret.3)
//add                    // returns fib(n-1) + fib(n-2)
@SP
M = M-1
A = M
D = M
A = A-1
M = D+M
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
(end)
@end
0;JMP
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
@FibonacciElement.0$ret.1
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
@FibonacciElement.Sys.init
0;JMP
(FibonacciElement.0$ret.1)
//// This file is part of www.nand2tetris.org
//// and the book "The Elements of Computing Systems"
//// by Nisan and Schocken, MIT Press.
//// File name: projects/08/FunctionCalls/FibonacciElement/Sys.vm
//
//// Pushes a constant, say n, onto the stack, and calls the Main.fibonacii
//// function, which computes the n'th element of the Fibonacci series.
//// Note that by convention, the Sys.init function is called "automatically" 
//// by the bootstrap code.
//
//function Sys.init 0
(FibonacciElement.Sys.init)
//push constant 4
@4
D = A
@SP
M = M+1
A = M-1
M = D
//call Main.fibonacci 1   // computes the 4'th fibonacci element
@FibonacciElement.Sys.init$ret.2
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
D = D + A
@SP
D = M - D
@ARG
M = D
@SP
D = M
@LCL
M = D
@FibonacciElement.Main.fibonacci
0;JMP
(FibonacciElement.Sys.init$ret.2)
//label WHILE
(FibonacciElement.Sys.init$WHILE)
//goto WHILE              // loops infinitely
@FibonacciElement.Sys.init$WHILE
0;JMP
(end)
@end
0;JMP
