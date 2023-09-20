


class NewNight():
    def __init__(self, knightID, position, teamColor = "*"):
        self.knightID = knightID
        self.position = position
        self.teamColor = teamColor
        
    def is_valid_square(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7
        
    def getValidMoves(self, position, board):
        self.position = position
        self.board = board
        validMoves = []
        column, row = self.getPosition(position)

        print(f"Current position is: {position}")
        knight_moves = [(1, 2), (-1, 2), (2, 1), (-2, 1), (1, -2), (-1, -2), (2, -1), (-2, -1)]

        for dx, dy in knight_moves:
            newx, newy = column + dx, row + dy
            if self.is_valid_square(newx, newy):
                spot = self.returnPosition(newx, newy)
                if spot in board:
                    if board[spot] != 0 and "*" in board[spot]:
                        print(f"Your Piece: {spot}")
                    elif board[spot] != 0 and "*" not in board[spot]:
                        print(f"Enemy piece {spot}")
                        validMoves.append(spot)
                    else:
                        validMoves.append(spot)

        return validMoves

        
    def moveBishop(self, moves, board):
        self.moves = moves
        self.board = board
        print("Valid moves are:")
        for item in moves:
            print(item)
            
        choice = input("Choose your move: ")
        if choice in moves:
            board[choice] = self.knightID
            
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
    