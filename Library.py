 len ("word")
4
>>> len ("word") + len ("square")
10
>>> programA = ['a','b','c','d']
>>> programB = ['A','B','C','D']
>>> programC = programA + programB
>>> programC
['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
>>> programD = [1,2,3,4]
>>> programC = programC + programD
>>> programC
['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', 1, 2, 3, 4]
>>> programC[9] = []
>>> programC[5:9] = programD
>>> progarmC
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'progarmC' is not defined
>>> programC[9:] = []
>>> programC[5:9] = programD
>>> programC
['a', 'b', 'c', 'd', 'A', 1, 2, 3, 4]
>>> a = ['a','b','c','d','e']
>>> b = ['A','B','C','D','E']
>>> c = a + b
>>> c
['a', 'b', 'c', 'd', 'e', 'A', 'B', 'C', 'D', 'E']
>>> c = b + a
>>> c
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
>>> d = [1,2,3,4,5]
>>> c = c + d
>>> c
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]
>>> c[9:] = []
>>> c[5:9] = d
>>> c
['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]
>>> len [c]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len ['c']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len (c)
10
>>> a = [10,20,30,40,50]
>>> b = [60,70,80,90,100]
>>> c = [110,120,130,140,150]
>>> x = [a,b,c]
>>> x
[[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]
>>> x[0][]
  File "<stdin>", line 1
    x[0][]
         ^
SyntaxError: invalid syntax
>>> x [0][]
  File "<stdin>", line 1
    x [0][]
          ^
SyntaxError: invalid syntax
>>> x [][3]
  File "<stdin>", line 1
    x [][3]
       ^
SyntaxError: invalid syntax
>>> x [1][2]
80
>>> x [][]
  File "<stdin>", line 1
    x [][]
       ^
SyntaxError: invalid syntax
>>> x [0][0]
10
>>> x [1][1]
70
>>> x[]
  File "<stdin>", line 1
    x[]
      ^
SyntaxError: invalid syntax
>>> x[1][2] + x[2][0]
190
>>> x [0][1] - x [2][1]
-100

>>> Fibonacci
char Dec   Binary       Hex
H => 72 => 01001000 =>  48
e => 101=> 01100101 =>  65
l => 108=> 01101100 =>  6C
l => 108=> 01101100 =>  6C
o => 111=> 01101111 =>  6F
spcae =>   => 00100000 => 20
W => 119 => 01010111 =>   57
o => 111 => 01101111 =>   6F
r => 114 => 01110010 =>   72
l => 108 => 01101100 =>   6C
d => 100 => 01100100 =>   64

python programming
