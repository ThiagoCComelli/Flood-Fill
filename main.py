from Floor import *
import sys

def setup():
    while True:
        op, message = floor.nextPass()
        if op:
            continue
        else:
            print(message)
            break

try:
    file = sys.argv[1]
    extension = 'png'
    if len(file.split(".")) != 1:
        extension = file.split(".")[1]
        file = file.split(".")[0]

    floor = Floor(file,extension)
    setup()
except IndexError:
    print('Fail to exec, no args given')
except FileNotFoundError:
    print('No such file in directory ./mazes')
