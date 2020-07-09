from PIL import Image
import time


class Floor():
    def __init__(self):
        self.__completed = None
        self.__width = None
        self.__height = None
        self.__image = Image.open('Maze4.png')
        self.__floor = []
        self.__actives = []
        self.init()
    
    def init(self):
        idx = 0

        values = list(self.__image.getdata())
        self.__width,self.__height = self.__image.size


        self.__floor = [[0 for x in range(self.__width)] for y in range(self.__height)]

        for i in range(self.__width):
            for j in range(self.__height):
                if values[idx] == (0,0,0):
                    element = 1
                elif values[idx] == (0,255,0):
                    element = -1
                    self.__floor[i][j] = 1
                    self.__actives.append(str(i)+" "+str(j))
                elif values[idx] == (255,0,0):
                    if(i == 99 and j == 28):
                        print(values[idx])
                        break
                    element = -2
                else:
                    element = 0

                self.__floor[i][j] = element
                idx += 1

        self.nextPass()
        
    def getFloor(self):
        return self.__floor
    
    def checkFinal(self):
        if len(self.__actives) == 0:
            return True
        else:
            return False
    
    def nextPass(self):
        temp = []

        for i in self.__actives:
            element = i.split(" ")

            x = int(element[0])
            y = int(element[1])

            posNow = self.__floor[x][y]

            try:
                if self.__floor[x+1][y] == -2 or self.__floor[x-1][y] == -2 or self.__floor[x][y+1] == -2 or self.__floor[x][y-1] == -2:
                    print(f"FINAL ACHIEVED!\n{self.__floor[x][y]+1} steps of distance from start to finish!\n")
                    self.__completed = True

                if self.__floor[x+1][y] == 0 and x+1 >= 0 and x+1 < self.__width:
                    self.__floor[x+1][y] = posNow + 1
                    temp.append(str(x+1)+" "+str(y))
                    # if str(x+1)+" "+str(y) == '99 28':
                    #     print(f"{x} {y} 0")
                    #     break
                
                if self.__floor[x-1][y] == 0 and x-1 >= 0 and x-1 < self.__width:
                    self.__floor[x-1][y] = posNow + 1
                    temp.append(str(x-1)+" "+str(y))
                    # if str(x+1)+" "+str(y) == '99 28 1':
                    #     print(f"{x} {y}")
                    #     break

                if self.__floor[x][y+1] == 0 and y+1 >= 0 and y+1 < self.__height:
                    self.__floor[x][y+1] = posNow + 1
                    temp.append(str(x)+" "+str(y+1))
                    # if str(x+1)+" "+str(y) == '99 28 2':
                    #     print(f"{x} {y}")
                    #     break

                if self.__floor[x][y-1] == 0 and y-1 >= 0 and y+-11 < self.__height:
                    self.__floor[x][y-1] = posNow + 1
                    temp.append(str(x)+" "+str(y-1))
                    # if str(x+1)+" "+str(y) == '99 28 3':
                    #     print(f"{x} {y}")
                    #     break

            except:
                continue
            
            self.__actives = temp

        # print(self.__actives)
        # print(self.__floor[98][28])

        if not self.checkFinal():
            return True, ""
        elif self.__completed == True:
            return False, "FINAL ACHIEVED!"
        else:
            return False, "No path to the final!"


