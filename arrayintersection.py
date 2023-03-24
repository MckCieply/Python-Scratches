num1 = [1,2,3,4]
num2 = [7,6,5,4,3]

def arraysearch(num1, num2):
    results = []
    if(len(num1) < len(num2)):
        for num in num1:
            if num in num2:
                results.append(num)
                num2.remove(num)
    else:
        for num in num2:
            if num in num1:
                if num not in results:
                    results.append(num)
                    num1.remove(num)
    
    return results