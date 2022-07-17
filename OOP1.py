#Basic banking system

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def details(self):
        print(f"""Personal Data:
Name: {self.name}
Age: {self.age}
Gender: {self.gender} 
""")

class Bank(User):
    def __init__(self,name,age, gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self, amount): 
        self.balance += amount
        print(f"Balance has ben updated: ${self.balance}")
    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance ):
            print(f"Insufficient funds. Balance avalible: ${self.balance}")
        else: 
            self.balance = self.balance - self.amount
            print(f"Account balance has ben updated: ${self.balance}")

    def view_balance(self):
        self.details()
        print(f"Account balance: ${self.balance}")

u1= Bank("Alex", 20, "Male")

u1.deposit(200)

u1.withdraw(50)

u1.view_balance()