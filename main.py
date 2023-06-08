import pyautogui
import time
import pyperclip
import keyboard


# you will have to pip install a couple of these
# in your cmd type 
# pip install pyautogui
# pip install pyperclip

width, height = pyautogui.size()
time.sleep(10)
is_true = False
count = 0

start = time.time()
while is_true is False:
    if keyboard.is_pressed("a"):
        is_true = True
    pyautogui.click(665, 351, button='left')
    pyperclip.copy('Kian Copper')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(681, 516, button='left')
    pyperclip.copy('Jacob Fahey')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(683, 606, button='left')
    r, g, b = pyautogui.pixel(686, 498)
    while r != 175 and g != 212 and b != 213:
        r, g, b = pyautogui.pixel(683, 606)
        fr, rg, rb = pyautogui.pixel(683, 606)
        if r == 1 and g == 68 and b == 70:
            pyautogui.click(683, 606, button='left')
        pass
    pyautogui.click(686, 498, button='left')
    count += 1
    print(count)

print(count)
print(time.time() - start)
print(count / (time.time() - start))
