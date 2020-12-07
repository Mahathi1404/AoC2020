with open('input1.txt') as fhand:
	lines=fhand.readlines()

nums = [int(line.strip()) for line in lines]

snum=sorted(nums)
#print(snum)
i=0
j=len(nums)-1

while i<j:
	if snum[i]+snum[j]==2020:
		print(snum[i]*snum[j])
		break
	elif snum[i]+snum[j]<2020:
		i+=1
	else:
		j-=1

#three sum
for i in range(0,len(snum)-2):
	fix=snum[i]
	l=i+1
	r=len(snum)-1
	while(l<r):
		if fix+snum[l]+snum[r]==2020:
			print(fix*snum[l]*snum[r])
			break
		elif fix+snum[l]+snum[r]<2020:
			l+=1
		else:
			r-=1





