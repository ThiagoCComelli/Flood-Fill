from PIL import Image
import time


class Floor():
    def __init__(self,file,extension):
        self.__completed = False
        self.__width = None
        self.__height = None
        self.__image = Image.open(f'./mazes/{file}.{extension}')
        self.__newImage = None
        self.__floor = []
        self.__actives = []
        self.__imagesCreated = 0
        self.__session = 0
        self.__allImages = []
        self.init()
    
    def createImage(self):
        self.__newImage = Image.new("RGB",(self.__image.size))

        list_of_pixels_another = []

        for i in range(self.__width):
            for j in range(self.__height):
                if self.__floor[i][j] == 1:
                    list_of_pixels_another.append((0,0,0))
                elif self.__floor[i][j] == 0:
                    list_of_pixels_another.append((255,255,255))
                else:
                    list_of_pixels_another.append((255,0,0))
        
        self.__newImage.putdata(list_of_pixels_another)
        self.__newImage.save(f"./images/{self.__imagesCreated}.png")
        self.__allImages.append(Image.open(f'./images/{self.__imagesCreated}.png'))
        self.__imagesCreated += 1

    def createGif(self):
        self.createImage()
        name = self.__image.filename.split(".")[-2].split("/")[-1]
        self.__allImages[0].save(f'./output/{name}.gif',save_all=True,loop=0,append_images=self.__allImages[1:])
    
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
                    # if(i == 99 and j == 28):
                    #     print(values[idx])
                    #     break
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

        if(self.__session % 10 == 0):
            self.createImage()

        for i in self.__actives:
            element = i.split(" ")

            x = int(element[0])
            y = int(element[1])

            posNow = self.__floor[x][y]

            try:
                if self.__floor[x+1][y] == -2 or self.__floor[x-1][y] == -2 or self.__floor[x][y+1] == -2 or self.__floor[x][y-1] == -2:
                    if self.__completed == False:
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

        self.__session += 1

        if not self.checkFinal():
            return True, ""
        elif self.__completed == True:
            self.createGif()
            return False, "FINAL ACHIEVED!"
        else:
            self.createGif()
            return False, "No path to the final!"


