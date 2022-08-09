import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
# print(pyautogui.size())
# for i in range(10):
#       pyautogui.moveTo(100, 100, duration=0.25)
#       pyautogui.moveTo(200, 100, duration=0.25)
#       pyautogui.moveTo(200, 200, duration=0.25)
#       pyautogui.moveTo(100, 200, duration=0.25)
# print(pyautogui.position())
print("\033[H\033[J", end="")
# GoogleSheetlocation = pyautogui.locateOnScreen(r'C:\Users\SheepSpirit\Test\Google sheets logo.png', grayscale=True)
# print(GoogleSheetlocation)
im2 = pyautogui.screenshot('hello world.png')
im = pyautogui.screenshot(region=(0,0, 300, 400))