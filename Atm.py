


class atm():
    def __init__(self, name, number):
        self.number = number
        self.name = name
        
        
    def askNumber(self):
        number = input("Enter your card number:")
        if number == "1234":
            print("This is the correct pin ")




    def balanceCheck(self):
        name = input("What is your name: ")
        if name == "Aditya":
            balance = 75
            print("You have", 75, "dollars")

        
            

aditya = atm("Aditya", "1234")
aditya.askNumber()
aditya.balanceCheck()







