"""Create a chess piece

for value in dict fullBoard:
    create corresonding piece object at location
"""

class newChessPiece():
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.team = self.isWhite(name)
        self.pieceMovement = self.setPiece(name)
        
    def isWhite(self, name):
        if "-" in name:
            return False
        else:
            return True
        
    def setPiece(self, name):
        if "P" in name:
            return [1*x]
        elif "R" in name:
            return [-x, -y, x, y]
        elif "N" in name:
            return [[x+1, y+3], [x+1, y-3], [x-1, y+3], [x-1, y-3]]
        elif "B" in name:
            return [[x(x+1, y+1)], [x(x-1, y+1)], [x(x+1, y-1)], [x(x-1, y-1)]]
        elif "Q" in name:
            return [[x(x+1, y+1)], [x(x-1, y+1)], [x(x+1, y-1)], [x(x-1, y-1)], [-x, -y, x, y]]
        elif "K" in name:
            return [x+1, x-1, y+1, y-1, [x+1, y+1], [x+1, y-1], [x-1, y+1], [x-1, y-1]]
        else:
            return "Invalid Name"
    
    def capture():
        pass
    
    def exchange():
        pass
    
class Rook(newChessPiece):
    def __init__(self, value, other_val):
        super().__init__(value)
        self.other_val = other_val
        
    def move(self):
        pass
    
class Bishop(newChessPiece):
    def __init__(self, value, other_val):
        super().__init__(value)
        self.other_val = other_val
        
    def move(self):
        pass

class Knight(newChessPiece):
    def __init__(self, value, other_val):
        super().__init__(value)
        self.other_val = other_val
        
    def move(self):
        pass

class Queen(newChessPiece):
    def __init__(self, value, other_val):
        super().__init__(value)
        self.other_val = other_val
        
    def move(self):
        pass

class King(newChessPiece):
    def __init__(self, value, other_val):
        super().__init__(value)
        self.other_val = other_val
        
    def move(self):
        pass

class Pawn(newChessPiece):
    def __init__(self, name):
        super().__init__(name, position=None)
        
    def move(self):
        pass
    

testPiece = newChessPiece("P", "a2")

print(testPiece.position)