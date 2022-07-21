import hashlib

def sign_up():
    email = input("Please input your e-mail: ")
    password = input ("Please input your password: ")
    confirm_password = input("Input your password again: ")

    if password == confirm_password:
        enc = confirm_password.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("logins.txt","w") as f:
            f.write(email + "\n")
            f.write(hash1)
        print("You have registered successfully! ")
    #elif with wrong email
    else:
        print("Your passwords are not matching!")

    cont = input("Do you want to log in now?[Y/N")
    if cont in ["Y"]:
        log_in()
    elif cont in ["N"]:
        print("Understandable, have a great day")
    else:
        print("You have no idea whats happening around you do you")

def log_in():
    email = input("Please input your e-mail: ")
    password = input ("Please input your password: ")

    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("logins.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    if email == stored_email and auth_hash == stored_pwd:
        print("Logged in Successfully")
    else:
        print("Login failed! \n")


def selection():
    print("""
    Welcome! Please select whether you are already one of our users
    or you are new around here...
    Type 1 to sign-in
    Type 2 to Log-in
     """)
    choose = input("-->")
    if choose in ["1"]:
        sign_up()
    elif choose in ["2"]:
        log_in()
    else: 
        print("Seems like you dont really get it")
    
selection()