#Basic banking system

class User():
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
    def details(self):
        print(f"""Personal Data:
firstname: {self.fname}
lastname: {self.lname}
Age: {self.age}
Gender: {self.gender} 
""")

class Bank(User):
    def __init__(self,fname,lname, age, gender):
        super().__init__(fname,lname, age,gender)
        self.balance = 0

    def deposit(self, amount): 
        self.balance += amount
        print(f"Balance has ben updated: ${self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if(self.amount > self.balance ):
            print(f"Insufficient funds. Balance avalible: ${self.balance}")
        else: 
            self.balance = self.balance - self.amount
            print(f"Account balance has ben updated: ${self.balance}")

    def view_balance(self):
        self.details()
        print(f"Account balance: ${self.balance}")

d1 = input("""
What would you like to do?
a) Create an Account.
b) Log In
""")

if d1 in ["A", "a"]:
    d2_fname = input("Please input your first name: ")   
    d2_lname = input("Please input your last name: ")
    d2_age = input("Please input your age: " )
    d2_gender = input("Please input your gener(Male/Female/Neither): ")
    p1 = User(d2_fname, d2_lname, d2_age, d2_gender)

    

