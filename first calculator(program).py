#conditional statements(else,elif,if)>syntax
print("welcome to the calculator")
print("what calculation do u wanna perform?")
print("1,addiiton")
print("2,subtraction")
print("3,multiplication")
print("4,division")
func = int(input("enter the function u selected(1,2,3 or 4):"))
if(func > 4 or func < 1):
    print("i said 1 to 4")
    exit()
a = float(input('input the first number>'))
b = float(input("input the second number>"))
if(func == 1):
    print("sum =",a + b)
elif(func == 2):
    print("difference =",a - b)
elif(func == 3):
    print("product =",a * b)
elif(func == 4):
    if(b != 0):
        print("quotient =",a / b)
    else:
        print("cant divide by 0")