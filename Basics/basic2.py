# Type matters
a = 'hello ' + 'There'
b = 123
c = 106.2
d = -2

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Type conversiond

print(float(99) + 100)
e = 42
f = 42
print(f)
print(type(f))
g = float(f)
print(g)
print(type(g))

# String conversions

sval = '123'
print(sval)
print(type(sval))

ival = int(sval)
print(ival)
print(type(ival))
print(ival + 1)

# user input, input outputs string
nam = input('who are you? ')
print('Welcome', nam)

inp = input('Europe floor? ')
usf = int(inp) + 1
print('US Floor', usf)

width = 15
heigth = 12.0
print(heigth/3)
