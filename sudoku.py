board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["9",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

def checkboard(board):
    valid = True
    # Checking horizontaly if valid
    for row in board:
        avalible = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for element in row:
            if element in avalible:
                avalible.remove(element)
            elif element == ".":
                pass
            else:
                valid = False
                break
    
    #checking verticaly if valid
    for i in range(9):
        avalible = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        numbers = []
        for j in range(9):
            element = board[j][i]
            if element in avalible:
                avalible.remove(element)
            elif element == ".":
                pass
            else:
                valid = False
                break
    #checking 3x3 squares
    for i in range(2,9,3):
        for j in range(2,9,3):
            avalible = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for x in range(0,3):
                for y in range(0,3):
                    element = board[j-y][i-x]
                    if element in avalible:
                        avalible.remove(element)
                    elif element == ".":
                        pass
                    else:
                        valid = False
                        break
                    
    return valid
            
            
checkboard(board)