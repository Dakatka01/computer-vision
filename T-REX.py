import numpy as np
from PIL import ImageGrab
import cv2
import keyboard
import pyautogui as m
import time
from mss import mss

sct = mss()
x = 578
y = 349
width = 96
k = 0.265
m.moveTo(x + width, y)
ch = 0
m.click()
s = 19
t = 19
r = 0
def jump():
    keyboard.release('down')
    time.sleep(0.01)
    keyboard.press('space')
    time.sleep(0.03)
    keyboard.release('space')
    print("space")
    time.sleep(k)
    keyboard.press('down')
    print("down")
start_time = time.time()
bounding_box = {'top': 0, 'left': 0, 'width': 2440, 'height': 1080}
while True:
    # Захватываем текущий кадр экрана с использованием Pillow (PIL)
    printscreen_pil = sct.grab(bounding_box)
    frame = np.array(printscreen_pil, dtype=np.uint8)

    # Получаем цвет пикселя на расстоянии width от начальных координат (x, y)
    pixel_color = frame[y, x + width]

    # Проверяем изменение цвета и выполняем действие
    if np.any([247, 247, 247, 255] != pixel_color) or np.any([247, 247, 247, 255] != frame[y, x+width+1]) \
            or np.any([247, 247, 247, 255] != frame[y-6, x+width+1]):
        # if np.any([247, 247, 247, 255] != pixel_color) and np.any([247, 247, 247, 255] != frame[y, x+width+22]) or\
        #     np.any([247, 247, 247, 255] != pixel_color) and np.any([247, 247, 247, 255] != frame[y, x+width+26])\
        #         and ch < 2:
        #     time.sleep(0.03)
        #     print("sleep")
        # keyboard.press('down')
        jump()
        print(pixel_color, frame[y, x + width])


    # Сохраняем кадр в файл PNG
    #cv2.imwrite(f'frame_{frame_count}.png', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    elapsed_time = time.time() - start_time  # Вычислим прошедшее время

    if elapsed_time >= t:  # Если прошло 25 секунд
        if np.any([247, 247, 247, 255] != frame[y, x+width-3]) \
            and np.any([247, 247, 247, 255] != pixel_color) \
            and np.any([247, 247, 247, 255] != frame[y, x + width + 2]) \
            and np.any([247, 247, 247, 255] != frame[y - 4, x + width + 2]):
            jump()
        ch += 1
        if ch >= 3:
            s += 3
        if ch< 4:
            width += s
            print(f"Widt   {ch} increased to {width}")
        start_time = time.time()
        m.moveTo(x + width, y)
    if ch == 2 and r == 0:
        r += 1
        k = 0.21
        t = 18

        # Обработка нажатия клавиши 'q' для выхода из цикла
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
