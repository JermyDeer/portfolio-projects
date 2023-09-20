from Board import NewBoard
from Rook import NewRook
from Knight import NewKnight
from Bishop import NewBishop
from Queen import NewQueen
from King import NewKing
from Pawn import NewPawn

"""
Chess Game - Want to add online display when able. 

"""

game = NewBoard("Test Game")
grid = game.createGrid()
gridDict = game.createGridDict()

whitePieces = game.setWhite(grid)
pawn = NewPawn("R1", "a1", True)
print(whitePieces)

#Display Game Start
# print("Welcome! Ready to play some chess?")
# colorChoice = input("Select white or black as your color: (w/b)  ")
# if (colorChoice.lower() == 'b'):
#     colorChoice = "Black"
# else:
#     colorChoice = "White"
    
# print("Great! You chose {}.".format(colorChoice))
# if (colorChoice == 'White'):
#     print("White has the first move.")


        
    
#Board Setup
"""What is the best wat to setupt this board? DO i make a dictionary of
all the squares and their occupants? Or maybe I make objects and give
them a position quality? Does each piece need to be a unique object?"""
#R-K-B-K-Q-B-K-R
#P-P-P-P-P-P-P-P
#Chess Piece Objects

#move(choosePiece, chooseLocation, moveLocation)
    #check is a piece
    #check is your team
    #Check can move to location
    #move to location
#get current location
#move object
#check valid move
#check capture piece
#update object location

#Movement
# print("To make a move, first specify a piece then specify a grid coordinate")
# print("For instance: r1a to 7a.")
#Piece Capture
#Pawn Special Movement
#Rook Special Movement
