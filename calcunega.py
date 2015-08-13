ans = 0
value = 0
input = "6+-5"
digits = []
operator = ""
count = 0
cnum = 0

def solve(operator, value, ans):
    
    if operator == "+":
        ans = ans + value

    elif operator == "-":
        ans = ans - value
    elif operator == "#": 
    	ans = value + 0 
    return ans

for i in input:
    if i.isdigit():
        digits.append(i)
        value = "".join(digits)
        value = int(value)

    else:
    	count = count + 1
    	
       	digits = []
        if count == 2:
            
            operator = "#"

            ans = solve(operator, value, ans)
            count  = 0
            operator = "-"
        elif i == "+":
            operator = "+"
            ans = solve(operator, value, ans)
        elif i == "-":
            operator = "-"
            ans = solve(operator, value, ans)
       

        

ans = solve(operator, value, ans)

print ans