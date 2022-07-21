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

def login():
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


sign_up()
login()
    
