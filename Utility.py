def readInput(q): # q is a queue
    while True:
        # read input as string
        print(">> ");
        new_pos = raw_input("Position ('[x,y,z]'): ")
        print 'recieved %s'%new_pos
        if (new_pos == 'q'):
            q.put(new_pos)
            break

        # split string at spaces to form an array
        new_pos = new_pos.split(" ")

        # make sure the array is valid
        if len(new_pos) != 3:
            raise ValueError("Input is not an array of size 3.")

        # convert array elements from strings to ints
        for i in range(0,len(new_pos)):
            new_pos[i] = float(new_pos[i])
            
        q.put(new_pos)
        
    return new_pos
