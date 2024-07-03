
# 控制键盘
from pynput.keyboard import Controller as key_c1
import time

# 控制鼠标
from pynput.mouse import Controller,Button
# 键盘控制的函数
def keyboard_input(string):
    keyboard = key_c1()
    keyboard.type(string)

# 鼠标点击一次左键
def mouse_input():
    mouse=Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)
# 执行函数
def main(number,string):
    time.sleep(7)
    for i in range(number):
        keyboard_input(string)
        mouse_input()
        time.sleep(0.4)

if __name__ == '__main__':
    number = input('请输入执行次数:')
    string = input('请输入轰炸内容')
    main(int(number),string)
