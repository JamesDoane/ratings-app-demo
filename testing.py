squares = {x:x for x in range(1000)}
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
print(squares.get(999))
word = "foobar"
a = iter(word)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
r = lambda something: something.split()

a = "welcome to the thunderdome"
b = "you son of a bitch"

print(r(a)+r(b))

for x in r(a):
    print(x)

c = loop(r(a))
print(c)
