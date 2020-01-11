print (20 > 10)
print (20 == 10)
print (20 < 10)
print (bool("hello world"))
print (bool(20))

python conditions			
	Equals 						->	x == y
	Not Equals					-> 	x != y
	less than					->	x >  y
	less than or equal to 		->	x >= y 
	greater than				->	x <  y
	greater than or equal to	->	x <= y

or => boolean OR       => x or y 	=> x | y
and => boolean AND     => x and y 	=> x & y
not => boolean NOT     => not x 	=> 

If_Else_Statement.python

# If statement
x = 10
y = 5
if x > y:
	print ("x is greate than y")

#Elif statement
x = 70
y = 70
if x > y:
	print ('x is greater than y')
elif x == y:
	print (' x and y are equal')

#Else 

x = 50
y = 150
if x > y:
	print ('x is greate than y')
elif x == y:
	print ('x and y are equal ')
else:
	print ('x is less than y')

#Short Hand if

if x > y: print ('x is greater than y')

#Short hand If..Else
#I like it

x = 50
y = 150
print (x) if x > y else print (y)

#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > y:
	print ('all conditions are true')
else:
	print ('all conditions are false')

#Or is a logical Operator

x = 50
y = 40
z = 100
if x > y or z > y:
	print ('one of the conditions is ture')
elif x > y and z > y:
	print ('all conditions are true')
else:
	print ("nothing else")

#Nested If is If statement in if statments
x = 50
if x > 10:
	print ('x is ten')
else:
	print ('x is not ten.')
	if x > 10:
		print ('x is greater than 10')
	else:
		print ('No, x is not greater than 20')

if x > 10 or x != 10 or x > 20:
	print ('x is greater than 10 and 20')
else:
	print ('x is not greater than 10 & 20')

#Pass statement
x = 100
y = 50

if x > y:
	pass
	
#Pass Statement















