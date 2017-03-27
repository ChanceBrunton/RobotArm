
import create_object
from process import processFrame

# get object for one piece

o = processFrame()

# create string containing object attributes

string = o.printString()

print(string)


string = 'pencil,12.0,16.0,100,200'

o.readString(string)

print(o.name)
