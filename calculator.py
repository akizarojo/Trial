ans = 0
value = 0
input = "5+2-1"
digits = []
operator = []

def solve(m, value, ans):
    if m == "+-":
        ans = ans +- value   
    elif m == "+":
        ans = ans + value
       
    elif m == "-":
        ans = ans - value
        

    return ans

for i in input:
    if i.isdigit():
        digits.append(i)

        value = "".join(digits)
        value = int(value)
    else:
        digits = []

        if i == "+":
            operator.append("+")
            m= "".join(operator)

            
        elif i == "-":
            operator.append("-")
            m= "".join(operator)
    
        ans = solve(m, value, ans)     
             



        


ans = solve(m, value, ans)

print ans