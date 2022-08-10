import travel_questions as questions
import random

answer = [1,2,3,4,5]

def questions_order():
    questions_list = []
    for x in range(questions.Question.counter):
        questions_list.append(x+1)
    random.shuffle(questions_list)
    print(questions_list)
        

name = input("Please tell us your name: ")
print("""
TRAVEL DESTINATION FORM
Please answer using numbers 1-5 depending how you much you like given acitvity
where 1 is least 'n' 5 is most""")



