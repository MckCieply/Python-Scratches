
basic = 2 
k = int(input ("Number of rounds in tournament: "))
teams = 1
while k > 0 :                                   #Checking how much teams are competing basing on ammount of rounds
    teams  *= basic
    k -= 1

print("Number of teams in tournament: ", teams )
teams_numbers = []
for i in range(0, teams):                      #Creating list with all teams competing
    teams_numbers.append(i)


def halfing():
    half = len(teams_numbers) // 2
    print("\n", half)  

half_of_list = []
half_size = len(teams_numbers) // 2
for i in range(0, len(teams_numbers), half_size):
    half_of_list.append(teams_numbers[i:i+half_size])
print(half_of_list, len(half_of_list))

