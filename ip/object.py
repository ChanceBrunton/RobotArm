import create_object

obj = create_object.Piece("eraser", 12, 14, (12,12))

string = obj.printString()

print(string)

obj.readString(string)

print(obj.name)



