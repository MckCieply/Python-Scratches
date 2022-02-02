team_1 = int(input("First team: "))
team_2 = int(input("Second team: "))
when_meet = []
def search(group):
    when_meet = []
    if (team_1 in group and team_2 in group):
        when_meet.append(group)
        print(when_meet)
def result():
    print("Your teams will meet in: ", )
def power():
    global teams
    global all_rounds
    basic = 2 
    all_rounds = int(input ("Number of rounds in tournament: "))
    k = all_rounds
    teams = 1
    while k > 0 :                                   #Checking how much teams are competing basing on ammount of rounds
        teams  *= basic
        k -= 1
power()
print("Number of teams in tournament: ", teams )
all_teams = []
for i in range(0, teams):                      #Creating list with all teams competing
    all_teams.append(i)
# print("Teams that can meet in finals(",all_rounds,"round ): \n", all_teams)
if (all_rounds >= 2):
    mid = len(all_teams) // 2
    semi_final_1 = all_teams [:mid]
    search(semi_final_1)
    semi_final_2 = all_teams [mid:]
    search(semi_final_2)
    mid = len(semi_final_1) // 2
    if (all_rounds >= 3):
        quarter_final_1 = semi_final_1 [:mid]
        search(quarter_final_1)
        quarter_final_2 = semi_final_1 [mid:]
        search(quarter_final_2)
        mid = len(semi_final_2) // 2
        quarter_final_3 = semi_final_2 [:mid]
        search(quarter_final_3)
        quarter_final_4 = semi_final_2 [mid:]
        search(quarter_final_4)
        if(all_rounds >= 4):
            mid = len(quarter_final_1) // 2
            last_16_1 = quarter_final_1 [:mid]
            search(last_16_1)
            last_16_2 = quarter_final_1 [mid:]
            search(last_16_2)
            mid = len(quarter_final_2) // 2
            last_16_3 = quarter_final_2 [:mid]
            search(last_16_3)
            last_16_4 = quarter_final_2 [mid:]
            search(last_16_4)
            mid = len(quarter_final_3) // 2
            last_16_5 = quarter_final_3 [:mid]
            search(last_16_5)
            last_16_6 = quarter_final_3 [mid:]
            search(last_16_6)
            mid = len(quarter_final_4) // 2
            last_16_7 = quarter_final_4 [:mid]
            search(last_16_7)
            last_16_8 = quarter_final_4 [mid:]
            search(last_16_8)

result(when_meet)



