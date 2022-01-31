
import random

def my_game():
    game = ["rock","scissors","paper"]                      
    player_score = 0
    pc_score = 0
    while ( player_score < 3 and pc_score < 3):
        computer = random.choice(game)                      
        player = input("Rock, Paper or Scissors? ")         
        player = player.lower()                             
        if player == computer:                              
            print("\nTie!")
            print("\nPlayer " , player_score  , " : " , pc_score , " PC\n")
        elif player =="rock":
            if computer == "paper":
                print("\nYou lose!",computer.capitalize(),"covers",player.capitalize())
                pc_score += 1
                print("\nPlayer " , player_score  , " : " , pc_score , " PC\n")
            else:
                print("\nYou win!",player.capitalize(),"smashes ",computer.capitalize())
                player_score += 1
                print("\nPlayer " , player_score  , " : " , pc_score , " PC\n")
        elif player == "paper":
            if computer == "scissors":
                print("\nYou lose!",computer.capitalize(),"cuts",player.capitalize())
                pc_score += 1
                print("\nPlayer " , player_score  , " : " , pc_score , " PC\n")
            else:
                print("\nYou win!",player.capitalize(),"covers",computer.capitalize())
                player_score += 1 
                print("\nPlayer " , player_score  , " : " , pc_score , " PC\n")
        elif player == "scissors":
            if computer == "rock":
                print("\nYou lose!",computer.capitalize(),"smashes",player.capitalize())
                pc_score += 1
                print("\nPlayer " , player_score  , " : " , pc_score , " PC\n")
            else:
                print("\nYou win!", player.capitalize(),"cuts",computer.capitalize())
                player_score += 1
                print("\nPlayer " , player_score  , " : " , pc_score , " PC\n")
                
        else: 
            print("Your input isnt Rock, Paper or Scissors. Only those 3 matters.")
    
    if (player_score == 3):
        print("\nYou won the game! Congrats! \n")
        choice = input("Do you want to try it one more time? (yes/no) ")
            
    else:
        print("\n AI have won over you! Shame on you! \n")
        choice = input("Do you want to try again.. loser? (yes/no) ")
    choice = choice.lower()
    if (choice == "yes"):
        print("\n \n Have fun! \n \n ")
        my_game(game, player_score = 0 , pc_score = 0)
    else: 
        print(" \n \n Thanks for playing! \n \n")


my_game()






