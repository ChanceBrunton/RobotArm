class ServoCommand:
        "Holds information pertaining to a single servo command."

        number = 0
        pulse = 0
        speed = 0

        def __init__(self,_number,_pulse,_speed):
            number = _number
            pulse = _pulse
            speed = _speed
