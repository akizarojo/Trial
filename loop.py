

lists = []

lists = []
for i in range(0, 30):
	
	if len(lists) == 0:
		lists.append(0)
	elif len(lists) == 1:
		lists.append(1)
		
	else:
		m = lists[-2]
		a = lists[-1]
		s = m+a
		lists.append(s)
print lists


	

	

    
