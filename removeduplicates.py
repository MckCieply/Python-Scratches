numbers = [1,2,2,2,3,4,5,6]
for i in numbers:
    ammount = 0
    for y , j in enumerate(numbers):
        if j == i:
            if ammount > 0:
                numbers[y] = "_"
            ammount += 1
            
print (numbers)
    