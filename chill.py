n=int(raw_input(""))
degree=[]
xor=[]
deg1=[]
for i in range(n):
	g=raw_input("").split(" ")
	degree.append(int(g[0]))
	if int(g[0])==1:
		deg1.append(i)
	xor.append(int(g[1]))
print sum(degree)/2
l=len(deg1)
while l>0:
	if degree[deg1[0]]!=1:
		deg1.remove(deg1[0])
		l-=1
		continue
	print deg1[0], xor[deg1[0]]
	degree[xor[deg1[0]]]-=1
	if degree[xor[deg1[0]]]==1:
		deg1.append(xor[deg1[0]])
	else:
		l-=1
	xor[xor[deg1[0]]]=xor[xor[deg1[0]]]^deg1[0]
	deg1.remove(deg1[0])