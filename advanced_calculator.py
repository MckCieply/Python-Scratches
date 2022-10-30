def menu():
    print("""
          WELCOME IN ADVANCED CALCULATOR
          PLEASE CHOOSE WHAT WOULD YOU LIKE TO CALCULATE:
          1) MEDIAN
          """)
    choice = input("Pass a coresponding number: ")
    if choice is "1":
        print("You will calculate median now!")
        numbers_input(choice)

def numbers_input(choice):
    numbers_list = []
    wrong_counter = 0
    is_true = True
    print("Please input your numbers one at the time: ")
    while is_true is True:
        number = input("-->")
        if number is "":
            is_true = False
            print("Finishing collecting data..")
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
                 
    print(numbers_list)
def calculate_median(numbers_list):
    max, min = None
    for number in numbers_list:
        pass

menu()