input = "1+13"
a  = False
b= False
l = []
ans = 0
operator = False
count = 0

def answer(i, ans, a):
	if i == "+":
		l[:]= []
		ans = a + ans

	elif i == "-":
		l[:]= []
		ans = a - ans

	return ans


for i in input:
	if i.isdigit():	
		l.append(i)
		if a == False:
			a = "".join(l)
			a = int(a)
		elif b == False or len(l) != 0:
			b = "".join(l)
			b = int(b)
			

	else:
		if b != False and operator != False:

			if operator == "+":
				ans = a + b

			elif operator == "-":
				ans = a - b
		else:
			if i == "+":
				l[:]= []
				operator = "+"
			elif i == "-":
				l[:]= []
				operator = "-"
print ans
