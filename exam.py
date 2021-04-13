#1
x = int(5)
print(type(x))
#2
x = 'aa' == 'AA'
print(type(x))
#3
x = {i: i**2 for i in range(5)}
print(type(x))
x = set(list((5, 6, 7)))
print(type(x))
#5
a = {1: 1, 2: 4, 3: 9}
print(type(x))
x = a.get(4)
print(type(x))
#6
x = [].append('j')
print(type(x))
#7
for i in range(10):
	if i < 5:
	    x = 'hello'
	else:
	    x = 5
print(type(x))
#8
x = input('Enter and integer: ')
print(type(x))
#9
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b
print(type(x))
#10
def func(x, y=5):
	return x + y
x = func('Jaguar ', 'hunter')
print(type(x))