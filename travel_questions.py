
formula = "How much do you like "
question_list = []
class Question():
    def __init__ (self, destination, description):
        self.destination = destination
        self.description = description 

question_list = []

q_1 = Question("Lake",f"{formula} fishing? ")
q_2 = Question("Lake",f"{formula} sailing? ")
q_3 = Question("Lake",f"{formula} BBQ? ")
q_4 = Question("Sea", f"{formula} sunbathing? ")
q_5 = Question("Sea", f"{formula} swimming in salt water? ")
q_6 = Question("Sea", f"{formula} collecting shells? ")
q_7 = Question("Mountains",f"{formula} hiking? ")
q_8 = Question("Mountains", "Whether you prefer passive(1) or active(5) recreaction? ")
q_9 = Question("Mountains", "How much do you admire sights? ")
