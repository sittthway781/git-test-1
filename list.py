>>> word = "programming"
>>> square = "square"
>>> len (word) + len (square)
17
>>> cube = [10,20,30,45,50]
>>> cube
[10, 20, 30, 45, 50]
>>> cube.append(60,70)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)
>>> cube.append(60)
>>> cube
[10, 20, 30, 45, 50, 60]
>>> cube [3] = 40
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.append(4+3)
>>> cube
[10, 20, 30, 40, 50, 60, 7]
>>> cube.append(4*10+20%36)
>>> cube
[10, 20, 30, 40, 50, 60, 7, 60]

>>> programA = ['A','B','C','D','E']
>>> programB = ['a','b','c','d','e']
>>> programC = programA + programB
>>>
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
>>> programD = [1,2,3,4,5]
>>> programC = programC + programD
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]

>>> programC[9:]=[]
>>> programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd']
>>> programC[9:]
[]
>>> programC[5:9]=programD
>>> programC
['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]
>>> len (programC)
10
>>> programC[3:]
['D', 'E', 1, 2, 3, 4, 5]
>>> programC
['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5]
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
>>> x[1][2]
80
>>> x[1:2][1:2]
[]
>>> x[]
  File "<stdin>", line 1
    x[]
      ^
SyntaxError: invalid syntax
>>> x[] = x
  File "<stdin>", line 1
    x[] = x
      ^
SyntaxError: invalid syntax
>>> x[1][2] + x[2][0]
190
>>> x[0][1] * x[2][1]
2400