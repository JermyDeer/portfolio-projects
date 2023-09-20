


class NewPawn():
    def __init__(self, pawnID, position, teamColor = True):
        self.pawnID = pawnID
        self.position = position
        self.teamColor = teamColor
        
    def getValidMoves(self, position, board):
        self.position = position
        self.board = board
        validMoves = []
        column, row = self.getPosition(position)
        
        if row < 7:
            #possible spots are row +1, and row+2, in the same column
            r1 = self.returnPosition(column, row+1)
            r2 = self.returnPosition(column, row+2)
            #Also, capture to right and left diagonal
            c1 = self.returnPosition(column-1, row+1)
            c2 = self.returnPosition(column+1, row+1)
            
            if board[r1] == 0:
                validMoves.append(r1)
                if row == 1 and board[r2] == 0:
                    validMoves.append(r2)
                
            if board[c1] != 0:
                validMoves.append(c1)
                
            if board[c2] != 0:
                validMoves.append(c2)
        else:
            validMoves.append("Promotion!!!")
        
        return validMoves
    
    def movePawn(self, moves, squares):
        self.moves = moves
        self.squares = squares
        print("Valid moves are:")
        for item in moves:
            print(item)
            
        choice = input("Choose your move: ")
        if choice in moves:
            squares[choice] = "Pawn"
            
        return squares
        
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