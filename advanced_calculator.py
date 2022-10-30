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
            time.sleep(0.2)
        except:  
            wrong_counter +=1
            if wrong_counter > 3:
                print("You gave wrong input too many times, shutting down.")
                time.sleep(1)
                break
            else:
                 print("Wrong value, not a number, please try again.")
                 time.sleep(0.5)
    corresponding_calculator(choice)
    
def corresponding_calculator(choice):
    if choice == "1":
        print("Calculating median now.. ")
        time.sleep(1)
        calculate_median(numbers_list)

def calculate_median(numbers_list):
    numbers_list.sort()
    lenght = int(len(numbers_list))
    if lenght%2 == 0:
        median = (numbers_list[lenght//2] + numbers_list[lenght//2 - 1]) / 2
        print(f"Median from imputed values is equal to {median}.")
    elif lenght%2 == 1:
        median = numbers_list[lenght//2 - 1]
        median = int(median)
        print(f"Median from imputed values is equal to {median}.")
        

menu()