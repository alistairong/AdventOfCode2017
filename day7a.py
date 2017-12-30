from inputs import day7a

myArr = day7a.split("\n")
myTree = {}

for eachLine in myStr:
	line = eachLine.split(" -> ")
	parent = (line[0].split())[0]
	if len(line) > 1:
		children = line[1].split(", ")
		for child in children:
			myTree[child] = parent

def findingRoot(myChild):
	if myTree[myChild] == []:
		return myChild
	else:	
		print (myTree[myChild])
		return findingRoot(myTree[myChild])

print(findingRoot("wiasj"))

