#Sets

#includes a data type for sets.
#Curly barces or the set() function can be use to create sets.
basket = {'apple','orangeo','apple','pear','orange','banan'}
print (basket)
'orange' in basket
'pear' in basket

a = set ('abracadabra')
b = set ('alacazm')
a
a - b
a | b
a & b
a ^ b # !letters in a and b

a = {x for x in 'abaacadabra' if x not in 'abc'}
a

a = {x for x in 'abacadabra' if x not in 'alacazam'}

fruits = {'apple','banana','cherry','orange','kiwi','melon','mango'}
print ('cherry' in fruits)

fruits.add('cucumber')
fruits
fruits.update('grape','water melon')
fruits
fruits.remove('banana')
fruits
fruits.discard('kiwi')
fruits

>>>Dictionaries

tel = {'jack':4098,'sape':4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel ['irv'] = 4127
tel

list(tel)
sorted(tel)

"guido" in tel

"sape" not in tel
dict ([('sape',4139),('guido',4127),('jack',4098)])

{x:x**2 for x in (2,4,6)}
{x:x**3 for x in (1,2,3,4,5)}


dict(sape=4139,guido=4127,jack=4098)

knights = {'gallahad':'the pure', 'robin':'the brave'}
for k,v in knights.items():
	print (k,v)	#k means key => gallahad...., v means value => the pure...

for i,v in enumerate(['tic','tac','toe']):
	print (a,b)

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for a,b in zip (questions, answers):
	print ('what\s ur {0}? It is {1}.'.format(a,b))

	