import pyautogui
import time
#pg.moveTo(55,753,3)#mover o mouse
a = 0
while a != 100:
    pyautogui.click(610,709)#para dar o click no pesquisar
    pyautogui.typewrite("crazy mandou falar contigo eae mano de boa?") # simula a digitação da string, tecla a
    pyautogui.press('enter')
    #time.sleep(2)
    
    a = a + 1
