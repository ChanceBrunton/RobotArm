from Utility import *
import ArmControl as ac
import Queue
import threading

def repeatPickupTest(current_pos,initial_pos,obj_pos,goal_pos,ser):
        counter = 1
        while True:
            print('Run %d:'%counter);counter = counter+1
            try:
                print('\tPicking up object...')
                ac.openGrip(ser)        
                current_pos = ac.moveToXYZ(obj_pos,current_pos,ser)
                ac.closeGrip(ser)

                print('\tPutting in goal...')
                current_pos = ac.moveToXYZ(goal_pos,current_pos,ser)
                ac.openGrip(ser)

                print('\tReturning to origin...')
                current_pos = ac.moveToXYZ(initial_pos,current_pos,ser)
                ac.closeGrip(ser)
            except ValueError as err:
                print('ValueError: '),;print(err)

def loopTest(current_pos,ser):
        cmd_queue = Queue.Queue()
        t = threading.Thread(name='input',target=readInput,args=(cmd_queue,))
        t.start()
        while True:
                try:
                        new_pos = cmd_queue.get()
                        if (new_pos == 'q'):
                                break
                        ac.openGrip(ser)
                        current_pos = ac.moveToXYZ(new_pos,current_pos,ser)
                        ac.closeGrip(ser)
                except TypeError as err:
                        print("Current position could not be calculated. "\
                              +"\tNew or current position may be invalid.\n"+str(err))
                except ValueError as err:
                        print(err)
