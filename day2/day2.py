with open('input2.txt') as f:
	lines=list(map(lambda l: l.strip(), f.readlines()))
#print(lines)
new_l=[]
for i in lines:
	l=i.split()
	new_l.append(l)
#print(new_l)
validCount=0
for i in range(len(new_l)-1):
	ran,letter,passwaor=new_l[i][0],new_l[i][1][0],new_l[i][2]
	indx=ran.index('-')
	lo=int(ran[:indx])
	hi=int(ran[indx+1:])
	#print(letter)

	
	if ((letter==passwaor[lo-1]) and (letter is not passwaor[hi-1])) or ((letter is not passwaor[lo-1]) and (letter==passwaor[hi-1])):
		validCount+=1

print(validCount)


