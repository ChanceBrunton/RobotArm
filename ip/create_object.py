# create objects for "objects"

class Piece(object):
    name = ""
    angle = 0
    width = 0
    midpoint = (0,0)
 

    # constructor
    def __init__(self, name, angle, width, midpoint):
        self.name = name
        self.angle = angle
        self.width = width
        self.midpoint = midpoint

    def printString(self):
        output = ''
        output = output\
                 + self.name + ','\
                 + str(self.midpoint[0]) + ','\
                 + str(self.midpoint[1]) + ','\
                 + str(self.angle) + ','\
                 + str(self.width)
        return output

    def readString(self, string):
        parsed = string.split(',')
        self.name = parsed[0]
        self.midx = int(parsed[1])
        self.midy = int(parsed[2])
        self.angle = int(parsed[3])
        self.width = int(parsed[4])

def make_piece(name, angle, width, midpoint):
    piece = Piece(name, angle, width, midpoint)
    return piece


