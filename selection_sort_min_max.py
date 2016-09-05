import random
import datetime

list = []
for value in range(0,100):
	x = random.randint(0,10000)
	list.append(x)
print list	

before = datetime.datetime.now()

count = 0
max_count = 0

while count <= len(list) - 2 - max_count:
	min = list[count]
	max = list[count]
	new_min = False
	new_max = False
	for index in range( count + 1, len(list) - max_count ):
		if list[index] <= min:
			min = list[index]
			new_min = True
			min_index = index
		elif list[index] >= max:
			max = list[index]
			new_max = True	
			max_index = index
	if new_min == True:
		for element in range( min_index, count , -1 ):
			list[element] = list[element - 1]
		list[count] = min	
	if new_max == True:
		for item in range( max_index, len(list) - 1 - max_count ):
			list[item] = list[item + 1]
		list[len(list) - 1 - max_count] = max	
		max_count += 1	
	count += 1	

after = datetime.datetime.now()	

print list
print after - before
