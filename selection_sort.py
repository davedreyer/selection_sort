import random
import datetime

list = []
for value in range(0,100):
	x = random.randint(0,10000)
	list.append(x)
print list	

before = datetime.datetime.now()

count = 0

while count <= len(list) - 2:
	min = list[count]
	new_min = False
	for index in range( count + 1, len(list) ):
		if list[index] <= min:
			min = list[index]
			new_min = True
			sort_index = index
	if new_min == True:
		for element in range( sort_index, count , -1 ):
			list[element] = list[element - 1]
		list[count] = min	
	count += 1	

after = datetime.datetime.now()

print list
print after - before




