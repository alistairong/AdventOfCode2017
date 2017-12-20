myVar = """4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"""

myVar = myVar.split()
myVar = list(map(int, myVar))

#list to store visited patterns
past_patterns = [0]
cycle = 0    

#loop to find max value, and distribute max value throughout array
def my_loop():
    past_patterns.extend([str(myVar)])
    num_count = 0
    max_i = 0

    #finding index of array which has max value
    i = 0
    while i < len(myVar):
        if myVar[i] > myVar[max_i]:
            max_i = i
        i += 1

    #storing max value and setting value at that index to 0 
    num_count = myVar[max_i]
    myVar[max_i] = 0

    #distributing max value over all array indices
    j = 1
    while num_count > 0:
        num_count -= 1
        myVar[(max_i + j) % len(myVar)] += 1
        j += 1

#day6a part below
while str(myVar) not in past_patterns:
    my_loop()
    cycle += 1

#day6b part below
past_patterns = [0]
cycle2 = 0

while str(myVar) not in past_patterns:
    my_loop()
    cycle2 += 1

print(cycle2)
