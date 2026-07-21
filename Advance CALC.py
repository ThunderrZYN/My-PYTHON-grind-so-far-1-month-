#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-#
#ADVANCE CALCULATOR
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-#
print('''<<WELCOME TO CALCULATOR>>''')
while True:
    caclu = input("\nWHAT CALCULATION DO U WANNA PERFORM(*,+,-,/ OR quit): ").lower()
    if caclu not in ("*","+","-","/","quit"):
        print("enter a valid operator.")
        continue
    elif caclu == "quit":
         print("you ended the program")
         quit()
   
    else:
            while True:
                try:
                    a = float(input("\nENTER FIRST NUMBER: "))
                    b = float(input("ENTER SECOND NUMBER: "))
                except ValueError:
                     print("ENTER NUMBERS")
                     continue
                if caclu == "+":
                     print("sum is: ",a+b)
                     break
                elif caclu == "-":
                     print("difference is: ",a-b)
                     break
                elif caclu == "*":
                     print("product =",a * b)
                     break
                elif caclu == "/":
                     if(b != 0):
                         print("quotient =",a / b)
                     else:
                         print("cant divide by 0")
                         continue