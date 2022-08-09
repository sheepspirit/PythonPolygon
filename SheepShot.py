
# = Список команд

# == Алерт с кнопкой ОК
# pyautogui.alert('This displays some text with an OK button.')

# == Алерт с Ок и отмена
# pyautogui.confirm('This displays text and has an OK and Cancel button.')
# 'OK'

# == Введите текст и нажмите Ок
# pyautogui.prompt('This lets the user type in a string and press OK.')
# 'This is what I typed in.'

#Описание модулей и переменных
import pyautogui, sys
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

#--Программа

# size = (pyautogui.size())
# xMax = (size[0])
# yMax = (size[1])
# print(f"Разрешение вашего экрана: {xMax} на {yMax} пикселей")

# x1 = 0
# y1 = 0
# x2 = 500
# y2 = 500
# screenshotCoordinates = ( x1, y1, x2, y2 )
  
# im2 = pyautogui.screenshot('hello world.png',region=(screenshotCoordinates))

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

