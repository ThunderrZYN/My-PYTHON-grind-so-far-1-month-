import json
import os
#MAIN CLASS FOR BANK ACCOUNT
class Bank_acc:
    def __init__(self,filename: str = "account.json",balance: float = 0.0) -> None:
        self.balance = balance
        self.history = []
        self.owner = None
        self.file = filename
        self.load()

    def credit(self,amount: float = 0.0) -> float:
        self.balance += amount
        return self.balance

    def debit(self,amount: float = 0.0) -> float:
        self.balance -= amount
        return self.balance

    def balance_check(self):
        return self.balance

    def save(self):
        with open(self.file,"w") as file:
            database = {
                "owner":self.owner,
                "balance":self.balance,
                "history":self.history
            }
            json.dump(database,file)
    def load(self):
        if os.path.exists(self.file):
            with open(self.file,"r") as file:
                saved_data = json.load(file)
                self.balance = saved_data["balance"]
                self.owner = saved_data["owner"]
                self.history = saved_data["history"]
        else:
            self.owner = input("FIRST TIME SETUP;ENTER NAME: ")
            self.save()

#object bank   
bank = Bank_acc()

#AMOUNT INPUT ERROR HANDLING(VALIDATING)
def amountvalidator():
    while True:
        try:
            am = float(input("enter amount: "))
        except ValueError:
            print("enter numbers")
            continue
        if am < 0:
           print("Negative input error")
           continue
        else:
            return round(am,2)
#CORE ATM LOOP

while True:

    #INPUT FOR FUNCTION TO PERFORM AND VALIDATION
    
    try:
        cr_de = int(input("\n--welcome to ATM--------------------------------\nwhat u wanna do?\n1.credit\n2.debit\n3.check balance\n4.check payment history\n5.quit: "))
    except ValueError:
        print("\nERROR:enter valid input")
        continue
    if cr_de not in (1,2,3,4,5):
        print("\nInvalid input: (enter 1-5)")
        continue

    #CREDITING AMOUNT
    
    elif cr_de == 1:
        am = amountvalidator()
        print("\nadding amount...","$",am)
        bank.credit(am)
        bank.history.append(f"credited ${am}")
        bank.save()
        print("done")
        continue

    #CHECKING BANK BALANCE
   
    elif cr_de == 3:
        print(f"\nYour bank balance is ${bank.balance_check():.2f}")
        continue

    #CHECK HISTORY

    elif cr_de == 4:
        if not bank.history:
            print("no transactions yet")
        else:
            for index, transaction in enumerate(bank.history):
                print(f"{index + 1}, {transaction}")
        continue

    #QUITTING ATM

    elif cr_de == 5:
        print("\nquit atm")
        break

    #DEBITING AMOUNT

    elif cr_de == 2:
        #CALLING AMOUNT VALIDATOR
        am = amountvalidator()
        #OVERDEBUIT GLITCH CHECK
        if am > bank.balance_check():
            print("\nyou dont have enough money")
            continue
        #MAIN DEBITOR
        else:
            bank.debit(am)
            bank.history.append(f"debited ${am}")
            bank.save()
            print("\ndebiting amount...","$",am)
            print("done")
