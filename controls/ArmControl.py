def rotate(servo, angle, ser):
        pulse = angleToPulse(angle)
        ser.write("#"+str(servo)+"P"+str(pulse)+"S1000\r\n")
        return

def angleToPulse(angle):
    pulse = map_range(angle,-180,180,1200,1780)
    return 1500

def map_range(og_value, og_min,og_max,new_min,new_max):
    og_range = og_max - og_min
    new_range = new_max - new_min
    new_value = (((og_value-og_min)*new_range)/og_range)+new_min
    return new_value
