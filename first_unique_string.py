def firstUniqChar(s):
    for i, letter in enumerate(s):
        if letter not in s[:i] and letter not in s[i+1:]:
            return i
        
    return -1

firstUniqChar("loveleetcode")
    