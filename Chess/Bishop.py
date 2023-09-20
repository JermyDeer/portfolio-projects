


class NewBishop():
    def __init__(self, bishopID, position, teamColor = "*"):
        self.bishopID = bishopID
        self.position = position
        self.teamColor = teamColor
        
    def getValidMoves(self, position, board):
        self.position = position
        self.board = board
        validMoves = []
        column, row = self.getPosition(position)
    
        print(f"Current position is: {position}")
        
        # Move X, Y
        spot = self.returnPosition(column, row)
        check = True
        while check:
            column += 1
            row += 1
            spot = self.returnPosition(column, row)
            if row < 0 or column < 0 or row > 7 or column > 7:
                check = False  # Stop the loop if row or column becomes negative
            elif board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)
                
            
        print("---------------------------")
        print(validMoves)

        #Move -X, Y
        column, row = self.getPosition(position)
        spot = self.returnPosition(column, row)
        check = True
        while check:
            column -= 1
            row += 1
            spot = self.returnPosition(column, row)
            if row < 0 or column < 0 or row > 7 or column > 7:
                check = False  # Stop the loop if row or column becomes negative
            elif board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)
            
        print("---------------------------")
        print(validMoves)
            
        #Move X, -Y
        column, row = self.getPosition(position)
        spot = self.returnPosition(column, row)
        check = True
        while check:
            column += 1
            row -= 1
            spot = self.returnPosition(column, row)
            if row < 0 or column < 0 or row > 7 or column > 7:
                check = False  # Stop the loop if row or column becomes negative
            elif board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)

        print("---------------------------")
        print(validMoves)
        
        # Move -X, -Y
        column, row = self.getPosition(position)
        spot = self.returnPosition(column, row)

        check = True
        while check:
            column -= 1
            row -= 1
            spot = self.returnPosition(column, row)
            if row < 0 or column < 0 or row > 7 or column > 7:
                check = False  # Stop the loop if row or column becomes negative
            elif board[spot] != 0 and self.teamColor in board[spot]:
                print(f"Your piece at {spot}")
                print("Not a valid Move")
                check = False
            elif board[spot] != 0 and self.teamColor not in board[spot]:
                print(f"Enemy piece at {spot}")
                validMoves.append(spot)
                check = False
            else:
                validMoves.append(spot)

        print("---------------------------")
        print(validMoves)

        ######################
        return validMoves
        #######################
        
    def moveBishop(self, moves, board):
        self.moves = moves
        self.board = board
        print("Valid moves are:")
        for item in moves:
            print(item)
            
        choice = input("Choose your move: ")
        if choice in moves:
            board[choice] = self.bishopID
            
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
    