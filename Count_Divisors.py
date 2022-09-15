i,r,k=[int(x) for x in input().split()]
c=0
for i in range(i,r+1):
    if i%k==0:
        c+=1
print(c)