n=int(raw_input(""))
seven=n/7
left=n%7
four=0
flag=0
while 1>0:
	if left%4==0:
		four=left/4
		break
	left+=7
	seven-=1
	if seven<0:
		flag=1
		break
if flag==1:
	print "-1"
else:
	print "4"*four+"7"*seven


