from keyboard import *
from tkinter import *
from time import *
from pyautogui import *

b='''
自动点击器 
创作者:黄浩宇
版本:1.0
使用方法:
      1.自动点击器能够帮你自动在Windows窗口上完成点击的任务
      2.输入两次单击相隔的时间和任务执行次数后,点击开始采集,将鼠标的光标放在需要点击的位置上,按下数字键盘中的"1",程序将自动记录此时鼠标所在的位置，并将该位置添加入单击任务列表中,再将鼠标放在下一个需要单击的位置，重复上述操作。所有位置添加完成后，点击数字键盘中的"2",程序将完成任务列表的创建
      3.点击任务创建完成后，点击"开始点击"，程序将自动操作鼠标完成点击
注意:  1.此处说明的单击问间隔时间是相邻两次单击的时间，而不是两次任务执行相隔的时间
      2.单机间隔时间请不要设置太短，否则单击过快，电脑可能反应不及时
      3.程序中的点击均为单击
      4.程序开始运行后，会自动将程序窗口最小化,以防错误点击
'''
def a1():
    t=[]
    def a2():
        i=position()
        t.append(i)
    while True:
          add_hotkey('1',a2)
          wait('2')
    return(t)
def a3():
    w.iconify()
    u1=w2.get()
    u2=w5.get()
    o=0
    while o!=u2:
          for y in t:
              click(y)
              sleep(u1)
    o=o+1
def a4():
    f=Tk()
    f.geometry('500x500')
    Label(f,text=b).pack()
    
    
    
w=Tk()
w.geometry('250x250')
w1=Label(w,text="请输入两次单击间隔的时间和任务执行次数")
w1.pack()
w2=Entry(w)
w2.pack()
w5=Entry(w,)
w3=button(w,text="开始采集",command=a1)
w3.pack()
w4=button(w,text="开始点击",command=a3)
w4.pack()

w9=button(w,text="点击获取帮助",command=a4)
w9.pack()