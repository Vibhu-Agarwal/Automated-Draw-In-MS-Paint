import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

def currentMousePosition():
    try:
        mul = 0
        while True:
            position = str(pyautogui.position())
            print('\b'*mul+position, end = '', flush = True)
            mul = len(position)
    except:
        input('\nDone')

print(pyautogui.size())
currentMousePosition()
