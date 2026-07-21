print("PASSWORD GENERATOR\nDo you wanna generate a password??")
consent = input("yes or no: ").lower()

import string
import random

if consent in ["yes","y","ye","ys","ya"]:
    
    k = int(input("how many letters: "))
    
    n = "!@#$%^&*-_=+"
    passw = string.ascii_letters + n + string.digits

    password = random.choices(passw,k = k)
    print("".join(password))
else:
    print("bye")