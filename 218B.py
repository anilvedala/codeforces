l=map(int,raw_input("").split(" "))
n=l[0]
m=l[1]
maxi=map(int,raw_input("").split(" "))
mini=[]
for i in maxi:
	mini.append(i)
mini.sort()
max_cost=0
min_cost=0
#print mini,maxi
for i in range(n):
	c=max(maxi)
	maxi[maxi.index(c)]-=1
	max_cost+=c
	#print maxi
	if mini[0]==0:
		mini.remove(0)
	min_cost+=mini[0]
	mini[0]-=1
	#print mini
print max_cost,min_cost
