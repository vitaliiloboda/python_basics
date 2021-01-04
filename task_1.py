import time


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}

    def running(self):
        while True:
            print(f'\033[30m\033[41m{list(self.__color.keys())[0]}')
            time.sleep(self.__color.get(list(self.__color.keys())[0]))
            print(f'\033[30m\033[43m{list(self.__color.keys())[1]}')
            time.sleep(self.__color.get(list(self.__color.keys())[1]))
            print(f'\033[30m\033[42m{list(self.__color.keys())[2]}')
            time.sleep(self.__color.get(list(self.__color.keys())[2]))
            print(f'\033[30m\033[43m{list(self.__color.keys())[1]}')
            time.sleep(self.__color.get(list(self.__color.keys())[1]))


a = TrafficLight()
a.running()

#######################################################вариант 2########################################################

from tkinter import *


class TrafficLight:

    def __init__(self, parent):
        self.canv = Canvas(parent, width=205, height=605, bg="black")
        self.canv.pack()
        self.canv.create_oval(5, 5, 200, 200, fill='grey', tag='canv1')
        self.canv.create_oval(5, 205, 200, 400, fill='grey', tag='canv2')
        self.canv.create_oval(5, 405, 200, 600, fill='grey', tag='canv3')
        self.canv.after(0, self.red, 'canv1')
        self.canv.after(7000, self.yellow, 'canv2')
        self.canv.after(9000, self.green, 'canv3')

        self.seconds = 0
        self.label = Label(parent, text='0 s', font='Arial 30', width=10)
        self.label.pack()
        self.label.after(1000, self.time)

    def red(self, tag):
        color = 'red'
        self.canv.itemconfig(tag, fill=color)
        self.canv.after(7000, self.grey_red, tag)

    def grey_red(self, tag):
        color = 'grey'
        self.canv.itemconfig(tag, fill=color)
        self.canv.after(11000, self.red, tag)

    def grey_yellow(self, tag):
        color = 'grey'
        self.canv.itemconfig(tag, fill=color)
        self.canv.after(7000, self.yellow, tag)

    def grey_green(self, tag):
        color = 'grey'
        self.canv.itemconfig(tag, fill=color)
        self.canv.after(11000, self.green, tag)

    def green(self, tag):
        color = 'green'
        self.canv.itemconfig(tag, fill=color)
        self.canv.after(7000, self.grey_green, tag)

    def yellow(self, tag):
        color = 'yellow'
        self.canv.itemconfig(tag, fill=color)
        self.canv.after(2000, self.grey_yellow, tag)

    def time(self):
        self.seconds += 1
        self.label.configure(text=f'{self.seconds} s')
        self.label.after(1000, self.time)


root = Tk()
light = TrafficLight(root)
root.mainloop()
