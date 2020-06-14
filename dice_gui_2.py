#!/usr/bin/python
# -*- Coding: utf-8 -*-
import random
import tkinter
#from tkinter import font   「font]でエラーが出たので使わない

def moving_dice():         #「サイコロを振る」を押したあとの動作
    num = random.randint(1,6)
    print(num)　　　　　　　#確認用
    output.delete(0,tkinter.END)
    output.insert(0,num)     

window = tkinter.Tk()       #ウィンドウのタイトルや大きさ
window.title("サイコロ")
window.geometry('120x120')

label1 = tkinter.Label(text="サイコロ", bg="cornsilk3" )
label1.pack(side="top")

output = tkinter.Entry(width=10)
output.place(x=30,y=30)

buton = tkinter.Button(text="サイコロを振る",command=moving_dice)
buton.place(x=25,y=60)

window.mainloop()
