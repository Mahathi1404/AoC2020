with open('input5.txt') as f:
	lines=[l.strip() for l in f.readlines()]

maxS=0
def getRow(s):
	lrow=0
	hrow=127
	for i in s:
		if i=='F':
			hrow=(hrow+lrow)//2
		if i=='B':
			lrow=(hrow+lrow)//2+1
		#print(lrow,hrow)
	return max(lrow,hrow)

def getCol(s):
	lcol=0
	hcol=7
	for i in s:
		if i=='R':
			lcol=(hcol+lcol)//2+1
		if i=='L':
			hcol=(hcol+lcol)//2
		#print(lcol,hcol)
	return max(lcol,hcol)
	return 0

seat=[]
for i in lines:
	row=i[:7]
	col=i[7:]
	n_pos=0
	r=getRow(row)
	c=getCol(col)
	seat_no=r*8+c
	seat.append(seat_no)
	#print(r,c,seat_no)
	maxS=max(maxS,seat_no)
s=sorted(seat)
#print(s)
print(maxS)

#part 2

for j in range(len(s)-1):
	if s[j+1]-s[j]!=1:
		myseat=s[j+1]-1
		

print(myseat)