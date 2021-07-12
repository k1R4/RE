from z3 import *

s = Solver()
a,b,c,d,e,f,g,h,i,j = Ints('a b c d e f g h i j')
l = [a,b,c,d,e,f,g,h,i,j]
for k in l:
    s.add(k>0x40)
    s.add(k<=0x5A)
s.add(a == j-0x3)
s.add(b == i+0xe)
s.add(c == h-0x14)
s.add(d == g+0x6)
s.add((e+f)/2 == a)

s.check()
m = s.model()
print(m)
for k in l:
    print(chr(m[k].as_long()).lower(),end="")
print()
