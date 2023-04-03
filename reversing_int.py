def reverse(x):
    string = str(x)
    if string[0] != "-":
        string = string[::-1]
    else:
        string = string[1:]
        string = "-" + string[::-1]
        
    x = int(string)
    
    
    
reverse(-123)