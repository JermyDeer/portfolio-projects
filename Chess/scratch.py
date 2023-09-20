GRID_REF = {}
chessBoard = []     
columns = ["a", "b", "c", "d",
            "e", "f", "g", "h"]

def notMoved():
    return True

counter = 0
for item in columns:
    GRID_REF[item] = counter
    counter += 1

for rows in range(1, 9):
    row = []
    for column in columns:
        row.append(column + str(rows))
    chessBoard.append(row)

my_string = "h8"

x_cord = GRID_REF[my_string[0]]
y_cord = int(my_string[1]) - 1
chessBoard[y_cord][x_cord] = "AAA"

for row in reversed(chessBoard):
    print(row)
    
    
pos1 = "c3"
pos2 = "c4"

y_cord1 = int(pos1[1])-1
y_cord2 = int(pos2[1])-1

if (y_cord1 + 1 == y_cord2) or (notMoved() and (y_cord2 - y_cord1 == 2)):
    print("valid move for white pawn")
else:
    print("invalid move for white pawn")
    
def getCoordinates(square):
    GRID_REF = {}
    columns = ["a", "b", "c", "d",
            "e", "f", "g", "h"]
    
    counter = 0
    for item in columns:
        GRID_REF[item] = counter
        counter += 1
        
    x_cord = GRID_REF[square[0]]
    y_cord = int(square[1]) - 1
    print(x_cord)
    print(y_cord)
    
    return x_cord, y_cord

x, y = getCoordinates("d1")
print("-------")
print(x)
print(y)