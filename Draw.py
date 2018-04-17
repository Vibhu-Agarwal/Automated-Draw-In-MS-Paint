#-----------------------------------------------------------------------------
#Author: Vibhu Agarwal (github.com/Vibhu-Agarwal)
#About: Python Script to open MS-Paint in Windows10 and draw the words
#-----------------------------------------------------------------------------

import pyautogui, time

#-----------------------------------------------------------------------------
pyautogui.FAILSAFE = True           #Activating Failsafe feature of pyautogui:
                                        #Take the mouse pointer to upper-left
                                        #corner of the screen to stop
                                        #GUI-Automation
pyautogui.PAUSE = 0.5               #Specifying to take a pause(in s) between
                                    #every function call for gui-automation
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
screenwidth, screenheight = pyautogui.size()        #Screen Width & Height
p,q = int(0.11*screenwidth),int(0.26*screenheight)
print('Letter Width:',p)                            #p = Letter Width
print('Letter Height:',q)                           #q = Letter Height
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#------------------ Function to open Paint in Windows10 ----------------------

def openPaint():
    pyautogui.press('win')                      #Pressing Window Key
    pyautogui.typewrite("Paint",0.15)
    coordinates = pyautogui.locateOnScreen("Paint Icon.png")
    i = 1
    while coordinates == None and i<=10:
        coordinates = pyautogui.locateOnScreen("Paint Icon.png")
        i += 1
    if coordinates == None:
        print("Could not find Paint Icon")
        return False
    x,y,wid,hei = coordinates
    x += wid//2
    y += hei//2
    pyautogui.moveTo(x,y,duration=0.1)
    pyautogui.click()
    return True
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#------------------------ Functions to draw Letters --------------------------

def drawA(a,b):
    pyautogui.click(a+(p//2),b)
    pyautogui.dragTo(a,b+q,duration = 0.15)
    pyautogui.click(a+(p//2),b)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    pyautogui.click(a+(p//4),b+(q//2))
    pyautogui.dragTo(a+((3*p)//4),b+(q//2),duration = 0.15)
    
def drawB(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a,b+q,duration = 0.15)
    pyautogui.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+(9*q)//10,duration = 0.1)
    pyautogui.dragTo(a+p,b+(q//2 + ((9*q)//100)),duration = 0.1)
    pyautogui.dragTo(a+(p//4),b+(q//2),duration = 0.1)
    pyautogui.dragTo(a+p,b+(q//2 - ((9*q)//100)),duration = 0.1)
    pyautogui.dragTo(a+p,b+q//10,duration = 0.1)
    pyautogui.dragTo(a+(4*p)//5,b,duration = 0.1)
    pyautogui.dragTo(a,b,duration = 0.15)

def drawC(a,b):
    pyautogui.click(a+p,b+q//6)
    pyautogui.dragTo(a+(4*p)//5,b,duration = 0.1)
    pyautogui.dragTo(a+p//5,b,duration = 0.15)
    pyautogui.dragTo(a,b+q//6,duration = 0.1)
    pyautogui.dragTo(a,b+(5*q)//6,duration = 0.15)
    pyautogui.dragTo(a+p//5,b+q,duration = 0.1)
    pyautogui.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+(5*q)//6,duration = 0.1)
    
def drawD(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a,b+q,duration = 0.15)
    pyautogui.dragTo(a + (4*p)//5,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+(q - ((17*q)//100)),duration = 0.15)
    pyautogui.dragTo(a+p,b+((17*q)//100),duration = 0.15)
    pyautogui.dragTo(a + (4*p)//5,b,duration = 0.15)
    pyautogui.dragTo(a,b,duration = 0.15)

def drawE(a,b):
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a,b,duration = 0.15)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.click(a,b+q//2)
    pyautogui.dragTo(a+p//2,b+q//2,duration = 0.15)
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    
def drawF(a,b):
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a,b,duration = 0.15)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.click(a,b+q//2)
    pyautogui.dragTo(a+p//2,b+q//2,duration = 0.15)

def drawG(a,b):
    pyautogui.click(a+p,b+q//6)
    pyautogui.dragTo(a+(4*p)//5,b,duration = 0.1)
    pyautogui.dragTo(a+p//5,b,duration = 0.15)
    pyautogui.dragTo(a,b+q//6,duration = 0.1)
    pyautogui.dragTo(a,b+(5*q)//6,duration = 0.15)
    pyautogui.dragTo(a+p//5,b+q,duration = 0.1)
    pyautogui.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+(5*q)//6,duration = 0.1)
    pyautogui.dragTo(a+p,b+q//2,duration = 0.1)
    pyautogui.dragTo(a+p//2,b+q//2,duration = 0.1)
    
def drawH(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a,b+(q//2),duration = 0.15)
    pyautogui.dragTo(a+p,b+(q//2),duration = 0.15)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a,b+(q//2),duration = 0.15)
    pyautogui.click(a+p,b+q)
    pyautogui.dragTo(a+p,b+(q//2),duration = 0.15)
    
def drawI(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.click(a+(p//2),b)
    pyautogui.dragTo(a+(p//2),b+q,duration = 0.15)
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    
def drawJ(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.click(a+(p//2),b)
    pyautogui.dragTo(a+(p//2),b+(5*q)//6,duration = 0.15)
    pyautogui.dragTo(a+(2*p)//5,b+q,duration = 0.1)
    pyautogui.dragTo(a+p//10,b+q,duration = 0.1)
    pyautogui.dragTo(a,b+(5*q)//6,duration = 0.1)
    
def drawK(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a,b+q,duration = 0.15)
    pyautogui.click(a+p,b)
    pyautogui.dragTo(a,b+(q//2),duration = 0.15)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    
def drawL(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    
def drawM(a,b):
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a,b,duration = 0.15)
    pyautogui.dragTo(a+p//2,b+q//2,duration = 0.15)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    
def drawN(a,b):
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a,b,duration = 0.15)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    
def drawO(a,b):
    pyautogui.click(a,b+q//6)
    pyautogui.dragTo(a,b+(5*q)//6,duration = 0.15)
    pyautogui.dragTo(a+p//5,b+q,duration = 0.1)
    pyautogui.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+(5*q)//6,duration = 0.1)
    pyautogui.dragTo(a+p,b+q//6,duration = 0.15)
    pyautogui.dragTo(a+(4*p)//5,b,duration = 0.1)
    pyautogui.dragTo(a+p//5,b,duration = 0.15)
    pyautogui.dragTo(a,b+q//6,duration = 0.1)
    
def drawP(a,b):
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a,b,duration = 0.15)
    pyautogui.dragTo(a+(4*p)//5,b,duration = 0.15)
    pyautogui.dragTo(a+p,b+q//10,duration = 0.1)
    pyautogui.dragTo(a+p,b+(2*q)//5,duration = 0.1)
    pyautogui.dragTo(a+(4*p)//5,b+q//2,duration = 0.1)
    pyautogui.dragTo(a,b+q//2,duration = 0.1)
    
def drawQ(a,b):
    pyautogui.click(a,b+q//6)
    pyautogui.dragTo(a,b+(5*q)//6,duration = 0.15)
    pyautogui.dragTo(a+p//5,b+q,duration = 0.1)
    pyautogui.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+(5*q)//6,duration = 0.1)
    pyautogui.dragTo(a+p,b+q//6,duration = 0.15)
    pyautogui.dragTo(a+(4*p)//5,b,duration = 0.1)
    pyautogui.dragTo(a+p//5,b,duration = 0.15)
    pyautogui.dragTo(a,b+q//6,duration = 0.1)
    pyautogui.click(a+(p//2),b+(5*q)//6)
    pyautogui.dragTo(a+p,b+q,duration = 0.1)
    
def drawR(a,b):
    pyautogui.click(a,b+q)
    pyautogui.dragTo(a,b,duration = 0.15)
    pyautogui.dragTo(a+(4*p)//5,b,duration = 0.15)
    pyautogui.dragTo(a+p,b+q//10,duration = 0.1)
    pyautogui.dragTo(a+p,b+(2*q)//5,duration = 0.1)
    pyautogui.dragTo(a+(4*p)//5,b+q//2,duration = 0.1)
    pyautogui.dragTo(a,b+q//2,duration = 0.1)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    
def drawS(a,b):
    pyautogui.click(a+p,b+q//10)
    pyautogui.dragTo(a+(7*p)//8,b,duration = 0.1)
    pyautogui.dragTo(a+p//8,b,duration = 0.1)
    pyautogui.dragTo(a,b+q//10,duration = 0.1)
    pyautogui.dragTo(a,b+(4*q)//10,duration = 0.1)
    pyautogui.dragTo(a+p//8,b+(q//2),duration = 0.1)
    pyautogui.dragTo(a+(7*p)//8,b+(q//2),duration = 0.1)
    pyautogui.dragTo(a+p,b+(3*q)//5,duration = 0.1)
    pyautogui.dragTo(a+p,b+(9*q)//10,duration = 0.1)
    pyautogui.dragTo(a+(7*p)//8,b+q,duration = 0.1)
    pyautogui.dragTo(a+p//8,b+q,duration = 0.1)
    pyautogui.dragTo(a,b+(9*q)//10,duration = 0.1)
    
def drawT(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.click(a+(p//2),b)
    pyautogui.dragTo(a+(p//2),b+q,duration = 0.15)
    
def drawU(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a,b+(q - ((17*q)//100)),duration = 0.15)
    pyautogui.dragTo(a + p//5,b+q,duration = 0.1)
    pyautogui.dragTo(a + (4*p)//5,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+(q - ((17*q)//100)),duration = 0.1)
    pyautogui.dragTo(a+p,b,duration = 0.15)

def drawV(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+(p//2),b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    
def drawW(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+p//4,b+q,duration = 0.15)
    pyautogui.dragTo(a+p//2,b+q//2,duration = 0.15)
    pyautogui.dragTo(a+(3*p)//4,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    
def drawX(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    pyautogui.click(a+p,b)
    pyautogui.dragTo(a,b+q,duration = 0.15)
    
def drawY(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+p//2,b+q//2,duration = 0.15)
    pyautogui.dragTo(a+p//2,b+q,duration = 0.15)
    pyautogui.click(a+p,b)
    pyautogui.dragTo(a+p//2,b+q//2,duration = 0.15)
    
def drawZ(a,b):
    pyautogui.click(a,b)
    pyautogui.dragTo(a+p,b,duration = 0.15)
    pyautogui.dragTo(a,b+q,duration = 0.15)
    pyautogui.dragTo(a+p,b+q,duration = 0.15)
    
#-----------------------------------------------------------------------------

    
#-----------------------------------------------------------------------------
#----------- Dictionary, assigning functions to call for a letter ------------
    
drawLetter = {"A":drawA, "a":drawA, "B":drawB, "b":drawB, "C":drawC, "c":drawC,
"D":drawD, "d":drawD, "E":drawE, "e":drawE, "F":drawF, "f":drawF,
"G":drawG, "g":drawG, "H":drawH, "h":drawH, "I":drawI, "i":drawI,
"J":drawJ, "j":drawJ, "K":drawK, "k":drawK, "L":drawL, "l":drawL,
"M":drawM, "m":drawM, "N":drawN, "n":drawN, "O":drawO, "o":drawO,
"P":drawP, "p":drawP, "Q":drawQ, "q":drawQ, "R":drawR, "r":drawR,
"S":drawS, "s":drawS, "T":drawT, "t":drawT, "U":drawU, "u":drawU,
"V":drawV, "v":drawV, "W":drawW, "w":drawW, "X":drawX, "x":drawX,
"Y":drawY, "y":drawY, "Z":drawZ, "z":drawZ}
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#---------------------- Function to draw one word ----------------------------

def drawName(name,x,y,spacing): #name: takes one word (str)
                #x,y: coordinates of top left corner of thebounds for a letter
                #spacing: space between each letter
    for i,ch in enumerate(name):
        #print(x+i*(p+spacing),y)
        if x+i*(p+spacing) > screenwidth-p:
            print('"'+name+'"'+' went out of bound in width')
            return
        try:
            drawLetter[ch](x+i*(p+spacing),y)
        except:
            pass
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#---------- Function to draw multiple words: one below the other -------------
        
def drawNames(names,sleeptime,letter_spacing): #names: a list of words
                           #sleeptime: wait time before start drawing words
                           #letter_spacing: space between each letter in words
    screenwidth, screenheight = pyautogui.size()
    #print('Place the mouse pointer at its initial position\nYou have',sleeptime,'seconds') #Method1
    time.sleep(sleeptime)
    x,y = pyautogui.position()
    for i,name in enumerate(names):
        if y+i*((23*q)//20) > screenheight-q:
            print('"'+name+'"'+' went out of bound in height')
            return
        drawName(name,x,y+i*((23*q)//20),letter_spacing)
#----------------------------------------------------------------------------- 



#-----------------------------------------------------------------------------
names = input("Enter names: ")              #Input from the user
if openPaint():                             #if paint opened, then continue
    pyautogui.moveTo(int(0.06*screenwidth),int(0.3*screenheight)) #Method2
    drawNames(names.split(),sleeptime = 1,letter_spacing = 15)
        #Give a greater sleeptime(~5) for Method 1

#-----------------------------------------------------------------------------
# PS. You can skip calling openPaint() function, open Paint yourself
#     set the Paint to desired Background and Brushes, Pencils, thickness
#     and go with Method 1 and comment out the Method2 lines
#-----------------------------------------------------------------------------
