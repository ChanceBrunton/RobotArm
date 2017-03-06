def read_coords():
    # read input as string
    new_pos = raw_input("Position ('[x,y,z]'): ")

    # split string at spaces to form an array
    new_pos = new_pos.split(" ")

    # make sure the array is valid
    if len(new_pos) != 3:
        raise ValueError("Input is not an array of size 3.")

    # convert array elements from strings to ints
    for i in range(0,len(new_pos)):
        new_pos[i] = float(new_pos[i])
        
    return new_pos
