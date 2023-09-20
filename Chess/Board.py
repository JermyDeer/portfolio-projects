from Rook import NewRook
from Knight import NewNight
from Bishop import NewBishop
from Queen import NewQueen
from King import NewKing
from Pawn import NewPawn

"""Class: NewBoard
Accepts: string Name

Generates a new chess board with black and white pieces in their positions

Returns:
    _type_: _description_
"""

class NewBoard():
    #INIT Columns Dictionary
    COLUMNS = ["a", "b", "c", "d",
                "e", "f", "g", "h"]
    COLUMNS_DICT = {}
    num = 0
    for letter in COLUMNS:
        COLUMNS_DICT[letter] = num
        num += 1
    #-------------------------------
    print(COLUMNS_DICT)
        
    def __init__(self, gameName):
        self.gameName = gameName
        
        
    def createGrid(self):
        chessBoard = []
        
        for rows in range(1,9):
            row = []
            for column in range(1,9):
                row.append(column)
            chessBoard.append(row)
                
        return chessBoard
    
    def createGridDict(self):
        columns = NewBoard.COLUMNS
        chessBoardDict = {}
        for row in range(1, 9):
            for column in columns:
                key = column + str(row)
                chessBoardDict[key] = 0
                
        return chessBoardDict
    
    def setWhite(self, board):
        self.board = board
        chessPieces = ['Rook', 'Night', 'Bishop', 'Queen', 'King', 'Pawn']
        startLine = ['Ra1', 'Nb1', 'Bc1', 'Qd1', 'Ke1', 'Bf1', 'Ng1', 'Rh1']
        startPawns = ['Pa2', 'Pb2', 'Pc2', 'Pd2', 'Pe2', 'Pf2', 'Pg2', 'Ph2']
        whitePieces = []
        
        for piece in startLine:
            for item in chessPieces:
                if piece[0] == item[0]:
                    newPieceClass = "New" + item
                    if newPieceClass in globals() and isinstance(globals()[newPieceClass], type):
                        createdPiece = globals()[newPieceClass](piece, piece[1:2])
                        whitePieces.append(createdPiece)
                    else:
                        print(f"Class {newPieceClass} not found")
                        
        
            
        
        
        return whitePieces
                
    def setBoard(self, board):
        self.board = board
        whitePieces = []
        #Make White's Pieces
        for pawnSpot in board[1]:
            whitePieces.append(NewPawn(pawnSpot))
        
        blackPieces = []
        #Make Black's Pieces
        for pawnSpot in board[6]:
            blackPieces.append(NewPawn(pawnSpot, False))
                
    def setPieces(self, emptyBoard):
        self.emptyBoard = reversed(emptyBoard)
        chessPieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Pawn']
        startPositions = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R',
                          'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
        
        #set pieces for white on board
        start_key = 'a1'
        end_key = 'h2'
        keys_to_iterate = list(emptyBoard.keys())[list(emptyBoard.keys()).index(start_key):list(emptyBoard.keys()).index(end_key) + 1]

        counter = 0
        for key in keys_to_iterate:
            emptyBoard[key] = startPositions[counter]
            counter += 1
        
        #set pieces for black on board
        blackStartPositions = startPositions[::-1]
        start_key = 'a7'
        end_key = 'h8'
        keys_to_iterate = list(emptyBoard.keys())[list(emptyBoard.keys()).index(start_key):list(emptyBoard.keys()).index(end_key) + 1]

        counter = 0
        for key in keys_to_iterate:
            emptyBoard[key] = "-" + blackStartPositions[counter]
            counter += 1
        
        return emptyBoard

board = NewBoard("Test")
gridDict = board.createGridDict()
whitePieces = board.setWhite("1")
print(whitePieces)



# Print the Board-----------------------
# rowHead = ["a", "b", "c", "d", "e", "f", "g", "h"]
# counter = 1
# for row in grid:
#     print(f'{counter}: {row}')
#     counter += 1
    
# stringHead = " | ".join(rowHead)
    
    
# print(f"   {stringHead}")
    




# gridDict = board.createGridDict(grid)
# setBoard = board.setPieces(gridDict)

#select object

# chooseLocation = input("What piece are you moving?  ")
# print("You picked the {} at {}".format(setBoard[chooseLocation], 
#                                        chooseLocation))

# moveLocation = input("Where will you move the piece?  ")
# print(setBoard[moveLocation])