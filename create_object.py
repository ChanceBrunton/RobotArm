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

def make_piece(name, angle, width, midpoint):
    piece = Piece(name, angle, width, midpoint)
    return piece


