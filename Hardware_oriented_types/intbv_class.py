#Explenation of intbv class
from myhdl import intbv

a = intbv(24)                   #unconstrained min, max values

print("\nValues for unconstrained intbv:")
print(a)
print(a.min)
print(a.max)
print(len(a))

b = intbv(24, min=0, max=25)    #constrained min, max

print("\nValues for inbv constrained min =0, max =25")
print(b)
print(b.min)
print(b.max)
print(len(b))

#allowed value range is 0 .. 24, and that 5 bits are required to represent the object

print("\nValue range check example:")
a = intbv(6, min=0, max=7)
print(len(a))

a = intbv(6, min=-3, max=7)
print(len(a))

a = intbv(6, min=-13, max=7)
print(len(a))
