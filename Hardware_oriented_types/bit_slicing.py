from myhdl import bin, intbv

a = intbv(24)
print(bin(a))
'11000'
a[4:1] = intbv(4)
print(bin(a[4:1]))
'100'
a[4:1] = 0b001
print(bin(a))
'10010'
a = intbv(18)
print(bin(a))
'11000'
print(bin(a[4:]))
'1000'
a[4:] = '0001'
print(bin(a))
'10001'
a[:] = 0b10101
print(bin(a))
'10101'

#################################
print("\n")
a = intbv(6, min=-3, max=7)
print(len(a))

b = a[4:]
print(b)
print(len(b))
print(b.min)
print(b.max)

print("\n")
a = intbv(-3)
print(bin(a, width=5))
'11101'
b = a[5:]
print(b)
print(bin(b))
'11101'

print("\n")
a = intbv(24)[5:]
print(a.min)
print(a.max)
print(len(a))

