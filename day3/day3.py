with open('input3.txt') as f:
	lines = f.readlines()

mapy=[l.strip() for l in lines]


row=0
col=0

treeC=0
'''
while row+1<len(mapy):
	col+=3
	row+=1

	if mapy[row][col%len(mapy[row])] == '#':
		treeC+=1
'''
slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]
total=1
for s in slopes:
	row=0
	col=0

	treeC=0
	while row+1<len(mapy):
		row+=s[1]
		col+=s[0]
		if mapy[row][col % len(mapy[row])]=='#':
			treeC+=1
	total*=treeC
print(total)