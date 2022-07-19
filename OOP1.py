#Basic banking system



class User():
    def __init__(self, fname, lname, age, gender, login, password):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.login = login 
        self.password = password

    def password_hash(self):
        lenght = len(self.password)
        hash = ""
        for i in range(lenght):
            hash += "*"
        return hash

    def details(self):
        print(f"""Personal Data:
Login: {self.login}
Password: {self.password_hash()}
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
    d2_login = input("Please input login you want to use: ")
    d2_password = input("Please input password of your choosing: ")
    p1 = User(d2_fname, d2_lname, d2_age, d2_gender)

elif d1 in ["B", "b"]:
    d2_login = input("Please input your login: ")
    d2_password = input("Please input your password: ")

# u1 = User("Alex","Nonimprotant", 20, "Male", "MckCieply", "4lit")

# u1.details()