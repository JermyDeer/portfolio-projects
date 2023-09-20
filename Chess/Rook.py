

class NewRook():
    def __init__(self, rookID, position, teamColor = "*"):
        self.rookID = rookID
        self.position = position
        self.teamColor = teamColor
        
    def getValidMoves(self, position, board):
        self.position = position
        self.board = board
        validMoves = []
        column, row = self.getPosition(position)
    
        print(f"Current position is: {position}")
        
        # Move Positive X
        spot = self.returnPosition(column, row)
        check = True
        while check:
            column += 1
            spot = self.returnPosition(column, row)
            
            if board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)
                
            if column == 7:
                check = False
        print("---------------------------")

        #Move Positive Y
        column, row = self.getPosition(position)
        spot = self.returnPosition(column, row)
        check = True
        while check:
            row += 1
            spot = self.returnPosition(column, row)
            if board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)
                
            if row == 7:
                check = False
        print("---------------------------")
            
        #Move Negative X
        column, row = self.getPosition(position)
        spot = self.returnPosition(column, row)
        check = True
        while check:
            column -= 1
            spot = self.returnPosition(column, row)
            
            if board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)

            if column == 0:
                check = False
        print("---------------------------")
        
        #Move Negative Y
        column, row = self.getPosition(position)
        spot = self.returnPosition(column, row)
    
        check = True
        while check:
            row -= 1
            spot = self.returnPosition(column, row)
            if board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)
                
            if row == 0:
                check = False
        print("---------------------------")
        
        return validMoves
        
    def moveRook(self, moves, board):
        self.moves = moves
        self.board = board
        print("Valid moves are:")
        for item in moves:
            print(item)
            
        choice = input("Choose your move: ")
        if choice in moves:
            board[choice] = "Pawn"
            
        return board
        
    def getPosition(self, position):
        self.position = position
        
        row = int(position[1]) - 1
        column = NewBoard.COLUMNS_DICT[position[0]]
        
        return column, row
    
    def returnPosition(self, column, row):
        self.column = column
        self.row = row
        position = NewBoard.COLUMNS[column] + str(row+1)
        
        return position