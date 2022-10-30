import time

def menu():
    print("""
          WELCOME IN ADVANCED CALCULATOR
          PLEASE CHOOSE WHAT WOULD YOU LIKE TO CALCULATE:
          1) MEDIAN
          """)
    global choice
    choice = input("Pass a coresponding number: ")
    numbers_input()

def numbers_input():
    global numbers_list
    numbers_list = []
    wrong_counter = 0
    is_true = True
    print("Please input your numbers one at the time: ")
    time.sleep(0.5)
    while is_true is True:
        number = input("-->")
        if number == "":
            is_true = False
            print("Finishing collecting data..")
            time.sleep(2)
            continue
        try:
            number = float(number)
            numbers_list.append(number)
        except:  
            wrong_counter +=1
            if wrong_counter > 3:
                print("You gave wrong input too many times, shutting down.")
                break
            else:
                 print("Wrong value, not a number, please try again.")
    corresponding_calculator(choice)
    
def corresponding_calculator(choice):
    if choice == "1":
        print("Calculating median now.. ")
        time.sleep(1)
        calculate_median(numbers_list)
def calculate_median(numbers_list):
    max, min = None, None
    for number in numbers_list:
        print(number)

menu()