n=int(raw_input(""))
l=[0]
for i in range(n):
    l.append(0)
s=map(int,raw_input("").split(" "))
for i in s:
    l[i]=1
for i in range(1,n+1):
    if l[i]==0:
        print i
        break
