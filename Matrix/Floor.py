class Floor():
    def __init__(self,size):
        self.__size = size
        self.__completed = False
        # self.__floor = [[0 for x in range(size)] for y in range(size)]
        self.__floor = [[1,1,1,1,1,1,1,1,1,1],
                        [-1,0,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,0,1],
                        [1,0,1,0,0,0,0,0,0,1],
                        [1,1,1,1,0,1,0,1,1,1],
                        [-2,0,0,1,0,1,0,0,0,1],
                        [1,1,0,1,0,0,0,1,0,1],
                        [1,0,0,1,1,1,1,1,0,1],
                        [1,0,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1]]
        self.__actives = []
        self.init()
        
    def getFloor(self):
        return self.__floor
    
    def checkFinal(self):
        if len(self.__actives) == 0:
            return True
        else:
            return False
    
    def init(self):
        for i in range(len(self.__floor)):
            for j in range(len(self.__floor[i])):
                if self.__floor[i][j] == -1:
                    self.__floor[i][j] = 1
                    self.__actives.append(str(i)+" "+str(j))
        
        self.nextPass()
    
    def nextPass(self):
        temp = []

        for i in self.__actives:
            element = i.split(" ")

            x = int(element[0])
            y = int(element[1])

            posNow = self.__floor[x][y]

            try:
                if self.__floor[x+1][y] == -2 or self.__floor[x-1][y] == 2 or self.__floor[x][y+1] == -2 or self.__floor[x][y-1] == -2:
                    print(f"FINAL ACHIEVED!\n{self.__floor[x][y]+1} steps of distance from start to finish!\n")
                    self.__completed = True

                if self.__floor[x+1][y] == 0 and x+1 >= 0:
                    self.__floor[x+1][y] = posNow + 1
                    temp.append(str(x+1)+" "+str(y))
                
                if self.__floor[x-1][y] == 0 and x-1 >= 0:
                    self.__floor[x-1][y] = posNow + 1
                    temp.append(str(x-1)+" "+str(y))


                if self.__floor[x][y+1] == 0 and y+1 >= 0:
                    self.__floor[x][y+1] = posNow + 1
                    temp.append(str(x)+" "+str(y+1))

                if self.__floor[x][y-1] == 0 and y-1 >= 0:
                    self.__floor[x][y-1] = posNow + 1
                    temp.append(str(x)+" "+str(y-1))

            except:
                continue
            
            self.__actives = temp

        if not self.checkFinal():
            self.nextPass()
        elif not self.__completed:
            print("No path to the final!\n")

