with open('input4.txt') as f:
	lines = f.readlines()
	data = [l.strip() for l in lines]

#print(data)

fields=['byr','iyr','eyr','hgt','hcl','ecl','pid']
validC=0

'''
#part 1
valid=True
pp=''
for i in data:
 	if i != '':
 		pp+=' '+i
 		#print(pp)
 	else:
 		for f in fields:
 			if f not in pp:
 				valid=False
 				break
 			else:
 				valid=True
 		if valid:
 			validC+=1

 		if is_valid(pp):
 			validC+=1
	 	pp='' 
def is_valid(pp):
	for f in fields:
		if f not in pp:
			return False
		if f is 'byr':
			if f != len

'''

#part 2
#print(data)
valid=True

pl=[]
final_list=[]
p=''
for i in data:
	if i != '':
		p+=' '+i#this would get me complete passport string 
	else:
		l=p.split()
		pl.append(l)
		p=''
if p:
	p+=' '+i
	l=p.split()
	pl.append(l)


for j in pl:
	ps={}
	for i in j:
		key=i[:3]
		value=i[4:]
		#print(key,value)
		ps[key]=value
	#print(ps)
	final_list.append(ps)


for i in final_list:
	valid=True
	#print(i)
	if len(i)<7:
		valid=False
	for j in fields:
		if j == 'cid':
			continue
		if j =='byr':
			if j not in i:
				valid=False
			elif  not 1920 <= int(i[j]) <= 2002:
				valid=False
		if j == 'iyr':
			if j not in i:
				valid=False
			elif not  2010 <= int(i[j]) <= 2020:
				valid=False
		if j == 'eyr':
			if j not in i:
				valid=False
			elif not 2020 <= int(i[j]) <= 2030:
				valid=False
		if j == 'hgt':
			if j not in i:
				valid=False
			elif i[j][-2:] == 'cm':
				if int(i[j][:-2])<150 or int(i[j][:-2])>193:
					valid=False
			elif i[j][-2:] == 'in':
				if int(i[j][:-2])<59 or int(i[j][:-2])>76:
					valid=False
			else:
				valid=False
		if j == 'hcl':
			if j not in i:
				valid=False
			elif i[j][0] != '#':
				valid=False
			elif (not i[j][1:].isalnum()) or len(i[j][1:])!=6:
				valid=False
		if j =='ecl':
			if j not in i:
				valid=False
			elif not (i[j] in ['amb','blu','brn','gry','grn','hzl','oth']):
				valid=False
		if j=='pid':
			if j not in i:
				valid=False
			elif len(i[j]) !=9:
				valid=False
	if valid == True:
		validC+=1
print(validC)


'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
ecl:amb
hgt:118 byr:1981 iyr:2019
hcl:#a97842 eyr:2021 pid:270790642
'''