def gcd(l):
    result=l[0]
    for x in l[1:]:
        if result<x:
            temp=result
            result=x
            x=temp
        while x!=0:
            temp=x
            x=result%x
            result=temp
        return result
n=int(input())
l=list(map(int,input().split()))[:n]
l=sorted(l)
a=gcd(l)
print(a)