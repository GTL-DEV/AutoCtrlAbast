import pyautogui
import time
import datetime
pyautogui.PAUSE = 0.6

time.sleep(10)
pyautogui.click(x=701, y=875)
time.sleep(5)
pyautogui.click(x=131, y=178)
time.sleep(5)
pyautogui.write("jose.cardoso@uscsonline.com.br")
time.sleep(6)
pyautogui.press('tab')
time.sleep(5)
pyautogui.press('tab')
time.sleep(5)
pyautogui.write("Planilhas Ctrl Abast/Compras")
time.sleep(4)
pyautogui.click(x=973, y=817)
time.sleep(5)
pyautogui.doubleClick(x=402, y=53)
time.sleep(4)
pyautogui.hotkey('ctrl', 'a')
time.sleep(4)
pyautogui.press('backspace')
time.sleep(4)
pyautogui.write("\s")
time.sleep(4)
pyautogui.press('backspace')
time.sleep(4)
pyautogui.write("\Servidor\servidor\Planilhas_JoseMario\Compras")
time.sleep(3)
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=281, y=348)
pyautogui.write("Auto Ctrl.Compras.xlsx")
time.sleep(5)
pyautogui.press('enter')
time.sleep(6)

pyautogui.click(x=973, y=817)
time.sleep(4)
pyautogui.doubleClick(x=402, y=53)
time.sleep(4)
pyautogui.hotkey('ctrl', 'a')
time.sleep(4)
pyautogui.press('backspace')
time.sleep(4)
pyautogui.write("\s")
time.sleep(4)
pyautogui.press('backspace')
time.sleep(4)
pyautogui.write("\Servidor\servidor\Planilhas_JoseMario\Analises Jan-Fev 2025")
time.sleep(3)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=281, y=348)
pyautogui.write("Ctrl Abast. TOPCON.xlsx")
time.sleep(5)
pyautogui.press('enter')
time.sleep(6)

pyautogui.click(x=973, y=817)
time.sleep(5)
pyautogui.doubleClick(x=402, y=53)
time.sleep(5)
pyautogui.hotkey('ctrl', 'a')
time.sleep(4)
pyautogui.press('backspace')
time.sleep(4)
pyautogui.write("\s")
time.sleep(5)
pyautogui.press('backspace')
time.sleep(5)
pyautogui.write("\Servidor\servidor\Planilhas_JoseMario\Compras")
time.sleep(5)
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=281, y=348)
pyautogui.write("Compras Geral Mar.xlsx")
time.sleep(5)
pyautogui.press('enter')
time.sleep(7)

#pyautogui.click(x=811, y=816)
pyautogui.click(x=831, y=826)
