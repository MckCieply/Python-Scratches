def isAnagram(s,t):
    s, checker = list(s),  list(s)
    t = list(t)
    for letter in s:
        if letter in t:
            checker.remove(letter)
            t.remove(letter)
            
    if(len(checker) == 0 and len(t) == 0):
        return True
    return False

isAnagram("rat", "car")