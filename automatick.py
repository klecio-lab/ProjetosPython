import pyautogui as pg
import pyautogui
import time
'''
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.5)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.5)  # move up
'''


'''position = pg.position()#posição do mouse
print(position)

pg.moveTo(540,707,3)#mover o mouse
pg.click(55,753)#para dar o click


a = 0
while a < 1000:
    pyautogui.typewrite("quer avacalhar é? ") # simula a digitação da string, tecla a
    pyautogui.press('enter')
    a = a + 1
    #avacalhar time.sleep(1)'''


'''
#pyautogui.typewrite("de boa?") # simula a digitação da string, tecla a
#pyautogui.press('enter')

a = pyautogui.pixel(206,429)#pegar cores rbg
print(a)
'''

pg.moveTo(55,753,3)#mover o mouse
pg.click(55,753)#para dar o click no pesquisar
pyautogui.typewrite("WhatsApp") # simula a digitação da string, tecla a
time.sleep(2)
pyautogui.press('enter')

#pg.moveTo(55,753,3)#mover o mouse
pg.click(55,753)#para dar o click no pesquisar
pyautogui.typewrite("chrome") # simula a digitação da string, tecla a
time.sleep(2)
pyautogui.press('enter')
