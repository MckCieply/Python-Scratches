answer_yes = ["Yes","Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]
print(""" 
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shelter to him? (Yes / No)
""")

ans1 = input(">>")
if ans1 in answer_yes:
    print("\n After 2 minutes, the Police came to your house, and ask you that whether the thief is in your house or not. (Yes / No)")
    
    ans2 = input(">>")
    if ans2 in answer_yes:
        print ("\n You are an honest person. He was a thief. You saved your life and made him pay for his crimes")
    elif ans2 in answer_no:
        print("\n You helped a thief. Now, you are going to jail for it.")
    else: 
        print("\n Thats the wrong answer, You are going to Jail. ")
elif ans1 in answer_no:
    print("\n Now he is trying to kill you. Will you overpower him? (Yes / No)")
    ans2 = input(">>")
    if ans2 in answer_yes:
        print("\n Congrats! You saved your life and helped capture dangerous criminal")
    elif ans2 in answer_no: 
        print("\n Well, you lost your life this way.")
    else:
        print("\n Thats the wrong answer, you died before you made decision.")
else:
    print("Thats the wrong answer.")