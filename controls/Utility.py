def read_coords():
    # read input as string
    new_pos = raw_input("Position ('[x,y,z]'): ")

    # split string at spaces to form an array
    new_pos = new_pos.split(" ")

    # convert array elements from strings to ints
    for i in range(0,len(new_pos)):
        new_pos[i] = int(new_pos[i])
        
    return new_pos
