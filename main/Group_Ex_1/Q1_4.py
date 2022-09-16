import math
#Group work 1
#Author: Alice Popov

#Q4
def area_of_triangle():
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    c = float(input("Enter c:"))
    
    t = (1/2) * (a + b + c)    
    S = math.sqrt(t*(t-a)*(t-b)*(t-c))
    print(S)
    
