import time

def menu():
    print("""
          WELCOME IN ADVANCED CALCULATOR
          PLEASE CHOOSE WHAT WOULD YOU LIKE TO CALCULATE:
          1) MEDIAN
          2) AVERAGE
          3) SUM
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
        number = input("--> ")
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

    if choice == "2":
        print("Calculating average.. ")
        time.sleep(1)
        calculate_average(numbers_list)
        
    if choice == "3":
        print("Calculating sum.. ")
        time.sleep(1)
        calculate_sum(numbers_list)

def calculate_median(numbers_list):
    numbers_list.sort()
    lenght = len(numbers_list)
    if lenght%2 == 0:
        median = (numbers_list[lenght//2] + numbers_list[lenght//2 - 1]) / 2
        print(f"\nMedian from imputed values is equal to {median}.")
    elif lenght%2 == 1:
        median = numbers_list[lenght//2 - 1]
        print(f"\nMedian from imputed values is equal to {median}.")
        
def calculate_average(numbers_list):
    lenght = (len(numbers_list))
    total = 0
    for number in numbers_list:
        total += number
    total /= lenght
    print(f"\nAverage from imputed values is {round(total,2)}.")

def calculate_sum(numbers_list):
    sum = 0
    for number in numbers_list:
        sum += number
    print(f'Sum of imputed values is equal to: {sum}.')

menu()