def function():
    for i in range(5):
        return i
def generator():
    for i in range(5):
        yield i             #return was replaced by yield

function()
generator()

print(function())
print(generator())

print("Values for generator, after using 'next' method 5 times")
g = generator()
a = g.__next__()
print(a)
a = g.__next__()
print(a)
a = g.__next__()
print(a)
a = g.__next__()
print(a)
a = g.__next__()
print(a)
#a = g.__next__()
#print(a)