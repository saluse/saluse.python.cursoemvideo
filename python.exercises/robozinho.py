import pyautogui
from time import sleep
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

pyautogui.write('Teste de inscrita automática. ')
sleep(2)
pyautogui.press('enter')
pyautogui.write('Teste aprovado')
pyautogui.press(['enter','enter'])
pyautogui.write(2 * 'Mais um!!!!')


