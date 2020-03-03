import random
import time
import copy
from os import system,name
def cellColor(cell):
    colors = ['w','g','o','r','b','y']
    if(cell == colors[0]):
        return [255,255,255]
    elif(cell == colors[1]):
        return [0,255,0]
    elif(cell == colors[2]):
        return [255,128,0]
    elif(cell == colors[3]):
        return [255,0,0]
    elif(cell == colors[4]):
        return [0,0,255]
    elif(cell == colors[5]):
        return [255,255,0]
    else:
        return None
class Cubes:
    @staticmethod
    def generateRandomMoveList(count):
        moves = ['U','L','F','R','B','D']
        moveList = []
        for i in range(0,count):
            r = random.random()
            e = random.randint(0,len(moves)-1)
            if r > 0.5:
                moveList.append(moves[e] + 'i')
            else:
                moveList.append(moves[e])

        return moveList
    @staticmethod
    def animateMoves(cube, moveList, spc):
        # spc = seconds per cycle
        for move in moveList:
            system('cls')
            cube.print()
            print("Next Move: " + move)
            cube.turn(move)
            time.sleep(spc)
        system('cls')
        cube.print()
        print("Final Cube")
    @staticmethod
    def reverseMoveList(moves):
        moves.reverse()
        for i in range(len(moves)):
            if len(moves[i]) == 1:
                moves[i] = moves[i] + 'i'
            else:
                moves[i] = moves[i][0]
        return moves
    def reverseMove(move):
        if len(move) == 1:
            return move + 'i'
        else:
            return move[0]


        
class Side:
    def __init__(self, color):
        self.c = color
        self.side = [[self.c,self.c,self.c], [self.c,self.c,self.c], [self.c,self.c,self.c]]
        #       c , c , c
        #       c , c , c
        #       c , c , c
    def cell(self, x, y):
        #       0  1  2
        #   0   c  c  c
        #   1   c  c  c
        #   2   c  c  c
        return self.side[y][x]
    def row(self,y):
        return self.side[y]
    def col(self,x):
        return [self.side[0][x], self.side[1][x], self.side[2][x]]
    def colrev(self,x):
        return [self.side[2][x], self.side[1][x], self.side[0][x]]
    def rowrev(self,y):
        return self.side[y][::-1]

    def setRow(self,y,row):
        self.side[y] = row
        return
    def setCol(self,x,col):
        self.side[0][x] = col[0]
        self.side[1][x] = col[1]
        self.side[2][x] = col[2]
        return
    def solved(self):
        base = self.cell(0,0)
        for row in self.side:
            for cell in row:
                if base != cell:
                    return False
        return True

    def r90(self):
        # A very hard-coded way of rotating a 3x3 matrix 90 degrees clockwise
        f = self.side
        leftCol = [f[0][0],f[1][0],f[2][0]]
        rightCol = [f[0][2],f[1][2],f[2][2]]
        topRow = [f[0][0],f[0][1],f[0][2]]
        botRow = [f[2][0],f[2][1],f[2][2]]
        f[0] = leftCol
        f[0].reverse()
        f[2] = rightCol
        f[2].reverse()
        f[1][0] = botRow[1]
        f[1][2] = topRow[1]
        self.side = f
        return

    
    def setCell(self,x,y,c):
        self.side[y][x] = c
        return
    def print(self):
        o = ''
        for i in range(0,3):
            for j in self.side[i]:
                o += j + ' '
            o += '\n'
        print(o)
                
    def arr(self):
        return self.side
class rCube:
    

    moves = ['U','L','F','R','B','D']
    def __init__(self):
        # Sides are initialized as 3x3 matrices each filled with whatever is in the constructor's field
        self.white = Side('w') #TOP
        self.green = Side('g') #FRONT
        self.orange = Side('o') #LEFT
        self.red = Side('r') #RIGHT
        self.blue = Side('b') #BACK
        self.yellow = Side('y') #BOTTOM
    def solved(self):
        if not (self.white.solved()):
            return False
        elif not (self.green.solved()):
            return False
        elif not (self.orange.solved()):
            return False
        elif not (self.red.solved()):
            return False
        elif not (self.blue.solved()):
            return False
        elif not (self.yellow.solved()):
            return False
        return True
    def print(self):
        #   This print function prints the cube as a 2d "folding diagram" in that the last
        #   side on the far right of the print is actually backwards.

        #   The prints will look like this (solved cube):
        #       w w w 
        #       w w w 
        #       w w w
        # o o o g g g r r r b b b
        # o o o g g g r r r b b b
        # o o o g g g r r r b b b
        #       y y y
        #       y y y
        #       y y y
        o = ''
        for i in range(0,3):
            o += '      '
            for j in self.white.arr()[i]:
                o += j + ' '
            o += '\n'
        #3245
        r1 = self.orange.arr()[0] + self.green.arr()[0] + self.red.arr()[0] + self.blue.arr()[0]
        r2 = self.orange.arr()[1] + self.green.arr()[1] + self.red.arr()[1] + self.blue.arr()[1]
        r3 = self.orange.arr()[2] + self.green.arr()[2] + self.red.arr()[2] + self.blue.arr()[2]
        s1 = ''
        s2 = ''
        s3 = ''

        for i in range(0,len(r1)):
            s1 += r1[i] + ' '
        s1 += '\n'
        for i in range(0,len(r2)):
            s2 += r2[i] + ' '
        s2 += '\n'
        for i in range(0,len(r3)):
            s3 += r3[i] + ' '
        s3 += '\n'

        o += s1 + s2 + s3
        e = ''
        for i in range(0,3):
            e += '      '
            for j in self.yellow.arr()[i]:
                e += j + ' '
            e += '\n'
        o += e
        print(o)
    def randomize(self):
        r = random.randint(50,200)
        for i in range(r):
            e = random.randint(0,len(self.moves))
            self.turn(self.moves[e - 1])
        return
    def turn(self, key):
        mod = False
        if len(key) > 1:
            mod = True
            key = key[0]
            
        #       w w w 
        #       w w w 
        #       w w w
        # o o o g g g r r r b b b
        # o o o g g g r r r b b b
        # o o o g g g r r r b b b
        #       y y y
        #       y y y
        #       y y y
        # For reference, we are treating the green side, or side 2, as the front.
        if key == 'U':
             #U:
            # s1: R90
            # s3 r1 to s5 r1
            # s5 r1 to s4 r1
            # s4 r1 to s2 r1
            # s2 r1 to s3 r1 - 
            self.white.r90()
            holder = self.orange.row(0)
            self.orange.setRow(0,self.green.row(0))
            self.green.setRow(0,self.red.row(0))
            self.red.setRow(0,self.blue.row(0))
            self.blue.setRow(0,holder)
            if(mod):
                self.turn('U')
                self.turn('U')
                
        elif key == "L":
            #L:
            # s3: r90
            # s1 c1 to s2 c1
            # s2 c1 to s6 c1
            # s6 c1 to s5 c3
            # s5 c1 to s1 c1
            self.orange.r90()
            holder = self.white.col(0)
            self.white.setCol(0,self.blue.colrev(2))
            self.blue.setCol(2,self.yellow.colrev(0))
            self.yellow.setCol(0,self.green.col(0))
            self.green.setCol(0,holder)
            if(mod):
                self.turn('L')
                self.turn('L')
        elif key == "F":
            #       w w w 
            #       w w w 
            #       w w w
            # o o o g g g r r r b b b
            # o o o g g g r r r b b b
            # o o o g g g r r r b b b
            #       y y y
            #       y y y
            #       y y y
            #F:
            # Green: R90
            # Orange C3 to White R3 reversed
            # White R3 to Red C1
            # Red C1 to Yellow R1 reversed
            # Yellow R1 to Orange C3
            self.green.r90()
            holder = self.orange.colrev(2)
            self.orange.setCol(2,self.yellow.row(0))
            self.yellow.setRow(0,self.red.colrev(0))
            self.red.setCol(0,self.white.row(2))
            self.white.setRow(2,holder)
            if(mod):
                self.turn('F')
                self.turn('F')
        elif key == "R":
            #R:
            # Red: R90
            # Green c3 to White C3
            # White C3 to Blue C1 Reversed
            # Blue C1 to Yellow C3 Reversed
            # Yellow C3 to Green C3
            self.red.r90()
            holder = self.green.col(2)
            self.green.setCol(2,self.yellow.col(2))
            self.yellow.setCol(2,self.blue.colrev(0))
            self.blue.setCol(0,self.white.colrev(2))
            self.white.setCol(2,holder)
            if(mod):
                self.turn('R')
                self.turn('R')
        elif key == "B":
            #B
            # Blue: R90
            # Red C3 to White R1
            # White R1 to Orange C1 reversed
            # Orange c1 to Yellow R3
            # Yellow R3 to Red C3 reversed
            self.blue.r90()
            holder = self.red.col(2)
            self.red.setCol(2,self.yellow.rowrev(2))
            self.yellow.setRow(2,self.orange.col(0))
            self.orange.setCol(0,self.white.rowrev(0))
            self.white.setRow(0,holder)
            if(mod):
                self.turn('B')
                self.turn('B')
        elif key == "D":
            #D
            # Yellow: R90
            # Green R3 to Red R3
            # Red R3 to Blue R3
            # Blue R3 to Orange R3
            # Orange R3 to Green R3
            self.yellow.r90()
            holder = self.green.row(2)
            self.green.setRow(2,self.orange.row(2))
            self.orange.setRow(2,self.blue.row(2))
            self.blue.setRow(2,self.red.row(2))
            self.red.setRow(2,holder)
            if(mod):
                self.turn('D')
                self.turn('D')
        #elif key == "Y":
            #Y:
            #Top
        return



def main():
    print('move: U')
    print('reverse: ' + Cubes.reverseMove('U'))
    print('move: Ui')
    print('reverse: ' + Cubes.reverseMove('Ui'))
if __name__ == '__main__':
    main()


