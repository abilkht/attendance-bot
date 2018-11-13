def miniproject(filename):
	f = open(filename, 'r')
	Bluelist = []
	List = []

	for line in f.readlines():
		List.extend(line.split())

	for c in List:
		if c not in Bluelist:
			Bluelist.append(c)
	return Bluelist

d = miniproject("database.txt")

def data(filename):
	f = open(filename, 'r')
	List = []
	Bluelist = []
	Studentlist = []

	for line in f.readlines():
		List.extend(line.split())
	a = len(List)
	b = {}

	for x in range(a - 1):
		if x % 2 == 0:
			b[List[x + 1]] = List[x]
	return b

a = data("databank.txt")

def check(L1,D1):
	for x in range(len(L1)):
		if L1[x] in D1:
			print (D1[L1[x]] + " is Present!")
print(check(d, a)) 