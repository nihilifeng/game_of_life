import random
import os
import time
class Universe():
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.content = dict()
        self.tostring = ""
        #create full universe space with 0s
        for hight in range(h):
            for width in range(w):
                #use x,y position to a tuple , and make it a key in content
                self.content[width,hight] = 0
        

    def randomize(self):
        out = dict()
        for y in range(self.h):
            for x in range(self.w):
                random_check = random.randint(0,2)
                if random_check == 0:
                    out[x,y] = 1
                else:
                    out[x,y] = 0
        self.content = out

    def calculate(self):
        out = dict()
        for y in range(self.h):
            for x in range(self.w):

                word=0
                try:
                    check = self.content[x-1,y+1]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                try:
                    check = self.content[x,y+1]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                try:
                    check = self.content[x+1,y+1]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                try:
                    check = self.content[x-1,y]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                try:
                    check = self.content[x+1,y]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                try:
                    check = self.content[x-1,y-1]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                try:
                    check = self.content[x,y-1]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                try:
                    check = self.content[x+1,y-1]
                    if check == 0:
                        pass
                    elif check == 1:
                        word+=1
                    else:
                        print('error')
                except:
                    pass
                if self.content[x,y] == 1:
                    if word < 2:
                        out[x,y] = 0
                    elif 2 <= word <=3:
                        out[x,y] = 1
                    elif word > 3:
                        out[x,y] = 0
                elif self.content[x,y] == 0:
                    if word == 3:
                        out[x,y] = 1
                    else:
                        out[x,y] = 0
        self.content = out


    def get_string(self):
        new_string = ""
        for y in range(self.h):
            for x in range(self.w):
                c = self.content[x,y]
                if c == 0:
                    new_string += " "
                else:
                    # new_string += u"\u2588"
                    new_string += '#'
            new_string +='\n'
        self.tostring = new_string




#set a function that clears all windows
def cls():
    #check the operating system , if it is windows , use cls command
    if os.name == 'nt':
        os.system('cls')
    else:
        #if it is mac or linux , use clear command
        os.system('clear')



# run app
universe = Universe(120,30)
universe.randomize()

while True:
    universe.get_string()
    print(universe.tostring)
    # universe.calculate()
    # time.sleep(1/2)
    universe.calculate()
    # time.sleep(1/25)
    cls()

# print(universe.toString)
# print(universe.content)