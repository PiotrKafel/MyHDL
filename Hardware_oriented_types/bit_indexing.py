from myhdl import bin, intbv

a = intbv(24)
print(bin(a))
'11000'
print(int(a[0]))
print(int(a[3]))

b = intbv(-23)
print(bin(b))
'101001'
print(int(b[0]))
print(int(b[3]))
print(int(b[4]))

print(bin(a))
'11000'
a[3] = 0
print(bin(a))
'10000'
print(a)

print(b)

print(bin(b))
'101001'
b[3] = 0
print(bin(b))
'100001'
print(b)

