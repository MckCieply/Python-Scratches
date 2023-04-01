board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
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
    
    
checkboard(board)