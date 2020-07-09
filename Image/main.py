from Floor import *
import time


floor = Floor()

while True:
    # print(time.time())
    op, message = floor.nextPass()
    if op:
        continue
    else:
        print(message)
        break

# for i in floor.getFloor():
#     print(*i)