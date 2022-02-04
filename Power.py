
basic = 2 
all_rounds = int(input ("Number of rounds in tournament: "))
k = all_rounds
teams = 1
while k > 0 :                                   #Checking how much teams are competing basing on ammount of rounds
    teams  *= basic
    k -= 1

print("Number of teams in tournament: ", teams )
all_teams = []
for i in range(0, teams):                      #Creating list with all teams competing
    all_teams.append(i)
print("Teams that can meet in finals(",all_rounds,"round ): \n", all_teams)
if (all_rounds >= 2):
    mid = len(all_teams) // 2
    semi_final_1 = all_teams [:mid]
    semi_final_2 = all_teams [mid:]
    print("Teams that can meet in first semi-final(",all_rounds - 1,"round ): \n", semi_final_1)
    print("Teams that can meet in second semi-final(",all_rounds - 1,"round ): \n", semi_final_2)
    mid = len(semi_final_1) // 2
    if (all_rounds >= 3):
        quarter_final_1 = semi_final_1 [:mid]
        quarter_final_2 = semi_final_1 [mid:]
        print("Teams that can meet in first quarter-final(",all_rounds - 2,"round ): \n", quarter_final_1)
        print("Teams that can meet in second quarter-final(",all_rounds - 2,"round ): \n", quarter_final_2)
        mid = len(semi_final_2) // 2
        quarter_final_3 = semi_final_2 [:mid]
        quarter_final_4 = semi_final_2 [mid:]
        print("Teams that can meet in third quarter-final(",all_rounds - 2,"round ): \n", quarter_final_3)
        print("Teams that can meet in fourth quarter-final(",all_rounds - 2,"round ): \n", quarter_final_4)
        if(all_rounds >= 4):
            mid = len(quarter_final_1) // 2
            last_16_1 = quarter_final_1 [:mid]
            last_16_2 = quarter_final_1 [mid:]
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_1)
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_2)
            mid = len(quarter_final_2) // 2
            last_16_3 = quarter_final_2 [:mid]
            last_16_4 = quarter_final_2 [mid:]
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_3)
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_4)
            mid = len(quarter_final_3) // 2
            last_16_5 = quarter_final_3 [:mid]
            last_16_6 = quarter_final_3 [mid:]
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_5)
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_6)
            mid = len(quarter_final_4) // 2
            last_16_7 = quarter_final_4 [:mid]
            last_16_8 = quarter_final_4 [mid:]
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_7)
            print("Teams that can meet in one LAST 16(",all_rounds - 3,"round ): \n", last_16_8)

print("To find when your teams meet please input their numbers ")
first_choice = int(input("First team number: "))
second_choice = int(input("Second team number: "))
if (all_rounds >= 4):
    if (first_choice and second_choice in last_16_1 or last_16_2 or last_16_3 or last_16_4 or last_16_5 or last_16_6 or last_16_7 or last_16_8):
        print('Your teams will meet in last 16 (',all_rounds - 3,'round )')
elif (first_choice and second_choice in quarter_final_1 or quarter_final_2 or quarter_final_3 or quarter_final_4):
    print('Your teams will meet in quarterfinals (',all_rounds - 2,'round )')
elif (first_choice and second_choice in semi_final_1 or semi_final_2):
    print('Your teams will meet in semifinals (',all_rounds - 1,'round )')
elif (first_choice and second_choice in all_teams):
    print('Your teams will meet in finals (',all_rounds,'round )')
else:
    print('Some of your teams is not listed in competition ')
