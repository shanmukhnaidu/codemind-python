def check(m,l):
    for i in l:
        if m%i != 0:
            return 0
    return 1
    
n=int(input())
l=list(map(int,input().split())) 
l=sorted(l)
m=max(l)
while l:
    if(check(m,l)):
        print(m)
        break
    else:
        m+=1