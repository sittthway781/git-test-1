>>> t = 12345, 54321, 'hello'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello')
>>> #tuples may be nested
>>> u =t,(1,2,3,4,5)
>>> u
((12345, 54321, 'hello'), (1, 2, 3, 4, 5))
>>> t[0]=8888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> v = ([1,2,3],[3,2,1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> fruits = ("apple", "banana", "cherry", "orange", "kiwi","melon","mango")
print (fruits[2:5])
>>> x = ('apple','banana','cherry','orange')
>>> y=list(x)
>>> y[1]='mango'
>>> x = tuple(y)
>>> x
('apple', 'mango', 'cherry', 'orange')


fruits = ("apple", "banana", "cherry", "orange", "kiwi","melon","mango")
x[4] = 'pineapple'
fruits
