import math
a,b,c=input().split()
A=int(a)
B=int(b)
C=int(c)
s=(A+B+C)/2
c=math.sqrt(s*(s-A)*(s-B)*(s-C))
print("%.2f"%c)