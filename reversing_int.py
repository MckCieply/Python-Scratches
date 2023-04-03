def reverse(x):
    string = str(x)
    if string[0] != "-":
        string = string[::-1]
    else:
        string = string[1:]
        string = "-" + string[::-1]
        
    x = int(string)
    
    if x >= 2**31 - 1 or x <= -2**31:
        return 0
    
    
reverse(-123)