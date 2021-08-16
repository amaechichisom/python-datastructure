from tkinter import *
import time

root=Tk()
root.geometry("1200x600")
myCanvas = Canvas(root, width=1200,height=600,bg="black")
myCanvas.pack()

def create_circle(x,y,r,canvasName):
    x0=x-r
    y0=y-r
    x1=x+r
    y1=y+r
    return canvasName.create_oval(x0,y0,x1,y1,fill="red")

def line(x1,y1,x2,y2,canvasName):
    return canvasName.create_line(x1,y1,x2,y2,fill="white",width=2,smooth=True)

x_first=600
y_first=50
vals="123456789"
circles=dict()
j=0
def create_circle(x,y,r,canvasName):
    x0=x-r
    y0=y-r
    x1=x+r
    y1=y+r
    return canvasName.create_oval(x0,y0,x1,y1,fill="red")
def line(x1,y1,x2,y2,canvasName):
    return canvasName.create_line(x1,y1,x2,y2,fill="white",width=2,smooth=True)
c=x_first
d=y_first
cf=1/(len(vals)-1)
def create_tree(c,d,i=0,mc=1.2):
    global vals,myCanvas,root,cf,j
    if i<len(vals):
        z=create_circle(c,d,20,myCanvas)
        root.update()
        m=Label(root,text=vals[i],bg="red",fg="white")
        m.config(font=("courier 16 bold"))
        m.place(x=c-8,y=d-12)
        circles[vals[i]]=(z,m)
        root.update()
        #time.sleep(1)
        if 2*i+1 <len(vals):
            x=line(c,d+30,c-90*mc,d+100,myCanvas)
            root.update()
            #time.sleep(0.5)
        create_tree(c-(100*mc),d+100,2*i+1,mc-mc*cf)
        if 2*i+2<len(vals):
            x=line(c,d+30,c+100*mc,d+100,myCanvas)
            root.update()
            #time.sleep(0.5)
        create_tree(c+(100*mc),d+100,2*i+2,mc-mc*2*cf)
        root.update()
create_tree(c,d)

create_circle(600,50,6,myCanvas)

line(40,20,40,120,myCanvas)
root.update()
time.sleep(4)