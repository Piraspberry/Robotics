#Written by Sounder on 14/05/2018

import tkinter as tk
from tkinter import *
import webbrowser
from tkinter import messagebox
import requests as r
import csv
import matplotlib as mpl
import numpy as np
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
import shutil
import os
import random
from random import randint
import re
from time import sleep
global n
class A:
    def __init__(self, root4,n):
        self.label=tk.Label(root4)
        self.label.pack()
        self.label.configure(text='nothing')
        self.count = 0
        self.update_label(n)
        

    def update_label(self,n):
        if (n!=0):
            self.label.configure(text = 'count: {}'.format(self.count))
            n=n-1
            self.count += 1
            self.label.after(1000, self.update_label(n)) # call this method again in 1,000 milliseconds
            

##def counter_label(label,n,counter):
##  def count():
##    counter += 1
##    label.config(text=str(counter))
##    label.after(1000, count)
##  if(n>=counter):
##      count()
##  else:
##      root4.destroy()
 
def counter_label(label,n):
    counts=0

    rand()    
    
        

def rand():
    
    root2=tk.Tk()
    root2.title("Auto updater window")
    Label(root2, text="Minimum value").grid(row=0)
    e2 = Entry(root2)
    e2.insert(10,"0")
    e2.grid(row=0, column=1)
    Label(root2, text="Maximum value").grid(row=1)
    e3 = Entry(root2)
    e3.insert(10,"100")
    e3.grid(row=1, column=1)
    Label(root2, text="Number of Terms").grid(row=2)
    e4 = Entry(root2)
    e4.insert(10,"10")
    e4.grid(row=2, column=1)

##            if(counter>=num):
##                flag=1
##        if(flag==0):
##            count()
##        if(flag==1):
##            root2.destroy()
##            root4.destroy()
    def gen():
##        try:
          x=[]
          y=[]
          a=int(e2.get())
          b=int(e4.get())
          n=int(e4.get())
          for i in range(1,n+1):
              x.append(random.randint(a,b))
              y.append(int(i))
          msg = tk.Message(root2, text = "Generated Numbers:")
          msg.config(font=('times', 12,'bold'))
          msg.grid()
          p=5
          q=5
          w=5
          s=5
          t=4
          for i in range(0,n):
##              try:
              r.get("https://api.thingspeak.com/update?api_key=974VJ8HS3E3NZNPF&field1=0"+str(x[i]))
##              except:
##                  messagebox.showinfo("Error","Please recheck your connection")
          
              msg = tk.Message(root2, text = x[i])
              msg.config(font=('times', 12))
              sleep(15)

              if((i>=10)&(i<20)):
                  msg.grid(row=s,column=1)
                  s=s+1
              elif((i>=20)&(i<30)):
                  msg.grid(row=p,column=2)
                  p=p+1
              elif((i>=30)&(i<40)):
                  msg.grid(row=q,column=3)
                  q=q+1
              elif((i>=40)&(i<50)):
                  msg.grid(row=r,column=4)
                  w=w+1
              else:

                  msg.grid()
          messagebox.showinfo("Info", "Updated Successfully")
##          root4=tk.Tk()
##          root4.title("Updation on Process")
##          label = tk.Label(root4, fg="green")
##          label.pack()
##          B7 = tk.Button(root4, text='Stop', width=25, command=root4.destroy)
##          B7.pack()
          
##          def update_label(num):
##              if (num!=0):
##                  self.label.configure(text = 'count: {}'.format(self.count))
##                  num=num-1
##                  self.count += 1
##                  self.label.after(1000, self.update_label(num))
##          update_label(n)
##          A(root4,n)
##          counts=0
##          for i in range(1,n+1):
##              sleep(1)
##              label.config(text=str(counts))
##          while(n>=counts):
##              sleep(1)
##              counts=counts+1
##              label.config(text=str(counts))
##          if(n<=counts):
##              root4.destroy()
##          counter_label(label,n)
##          root4.destroy()




##        except:
##          messagebox.showinfo("Error", "Please try again")
          e3.delete(0,END)
    tk.Button(root2, text='Generate', command=gen).grid(row=3, column=1)


    
##n=int(input("Enter terms of numbers to be generated"))
##a=int(input("Enter Minimum Term"))
##b=int(input("Enter Maximum Term"))
##x=[]
##y=[]
##for i in range(1,n+1):
##    x.append(random.randint(a,b))
##    y.append(int(i))
def messager(mssg):
    msg = tk.Message(root, text = mssg)
    msg.config(font=('times', 12))
    msg.pack()
def gotosimatic():
    messagebox.showinfo("Message", "Opening SIMATIC IOT2000 in your default broswer")
    url2 = 'https://w3.siemens.com/mcms/pc-based-automation/en/industrial-iot/pages/default.aspx'
    webbrowser.open_new(url2)


def downloadanddisplay():
    messager("Data log file has been downloaded as TempData.csv")
    a5=os.getcwd()
    a6=os.path.join(a5,"TempData.csv")
    a10=''
    for i in a6:
        if(i=='\\'):
            i='/'
        a10=a10+i
    print(a10)
    shutil.os.remove(str(a10))
    url1 = 'https://thingspeak.com/channels/413291/feed.csv'
    rr = r.get(url1, allow_redirects=True)
    open('TempData.csv', 'wb').write(rr.content)

    

def updationwin():

    root1=tk.Tk()
    root1.title("Sender App")
    Label(root1, text="Numeric Data").grid(row=0)
    e1 = Entry(root1)
    e1.insert(10," ")
    e1.grid(row=0, column=1)
    def updater():
        try:
            r.get('https://api.thingspeak.com/update?api_key=974VJ8HS3E3NZNPF&field1=0'+str(e1.get()))
            messagebox.showinfo("Info", "Updated Successfully")
        except:
            messagebox.showinfo("Error", "Please recheck your connection")
            updationwin()
        e1.delete(0,END)
    tk.Button(root1, text='Update', command=updater).grid(row=1, column=1)


def matgui():
    messager("Up-to-date graph is displayed")
    def draw_figure(canvas, figure, loc=(0, 0)):

        figure_canvas_agg = FigureCanvasAgg(figure)
        figure_canvas_agg.draw()
        figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

        canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
        tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
        return photo
    w, h = 700, 700
    window = tk.Tk()
    window.title("Change in Furnace Temperature with respect to a value propotional to time (Data ID)")
    canvas = tk.Canvas(window, width=w, height=h)
    canvas.pack()


   

    with open('TempData.csv', 'rU') as infile:
        reader = csv.DictReader(infile)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]
    X= data['entry_id']
    Y = data['field1']
    Y = [re.sub('0 ', '', item) for item in Y]
    for (i, item) in enumerate(Y):
        if item=='':
            Y[i] = '0'
    X=list(map(int,X))
    Y=list(map(int,Y))

    fig = mpl.figure.Figure(figsize=(5, 5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.plot(X, Y)

    fig_x, fig_y = 100, 100
    fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
    fig_w, fig_h = fig_photo.width(), fig_photo.height()
    tk.mainloop()
root = tk.Tk()
root.title("Simtic IoT 2040 Starter Application")
a1=str(os.getcwd())
a9=os.path.join(a1,"icon.ico")
##a2=a1+"/icon.ico"
a8=''
for i in a9:
    if(i=='\\'):
        i='/'
    a8=a8+i
print(a8)
    

a2=''
a3=os.path.join(a1,"siemenslogo.gif")
for i in a3:
    if(i=='\\'):
        i='/'
    a2=a2+i
print(a2)
##re.swap()
root.iconbitmap(str(a8))
logo = tk.PhotoImage(file=str(a2))

w1 = tk.Label(root, image=logo).pack(side="left")

texter = """Welcome, Let's get started!
""" 
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack(side="bottom")
w2 = tk.Label(root,compound=tk.CENTER,padx = 10,text=texter).pack()


    
def sender():
    updationwin()

def helloCallBack():
    
    messagebox.showinfo("Message", "Opening your visualization in your default broswer")
    url = 'https://thingspeak.com/channels/413291'
    webbrowser.open_new(url)
    


B0 = tk.Button(root,width=25, text ="Get to know IoT 2000 series", command = gotosimatic)
B0.pack(side="top")
B1 = tk.Button(root,width=25, text ="Visualize Data", command = helloCallBack)
B1.pack(side="bottom")
B2 = tk.Button(root,width=25, text ="Send Data", command = sender)
B2.pack(side="bottom")
B4=tk.Button(root,width=25, text ="Downlaod Data log", command = downloadanddisplay)
B4.pack(side="bottom")
B5=tk.Button(root,width=25, text ="Display Graph", command = matgui)
B5.pack(side="bottom")
B5=tk.Button(root,width=25, text ="Auto-update cloud", command = rand)
B5.pack(side="bottom")

root.mainloop()

