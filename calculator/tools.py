'''
Created on 2021年4月20日

@author: leesure
'''
from tkinter import  Button, Frame, StringVar
from tkinter.constants import SUNKEN,RAISED,GROOVE,RIDGE
from calculator import myBtn

def rowModules(mainWidget, *displayList, abColor, width, side, padx, pady):
    def startExec(btnIndex):
        varStr=StringVar()
        varStr.set(btnIndex)
    fr1=Frame(mainWidget)
    btn1 = Button(fr1, text="{0}".format(displayList[0]), activebackground=abColor, width=width, command=lambda:startExec(btn1["text"]))
    btn1.pack(side=side,padx=padx,pady=pady)
    btn2 = Button(fr1, text="{0}".format(displayList[1]), activebackground=abColor, width=width,command=lambda:startExec(btn2["text"]))
    btn2.pack(side=side,padx=padx,pady=pady)
    btn3 = Button(fr1, text="{0}".format(displayList[2]), activebackground=abColor, width=width,command=lambda:startExec(btn3["text"]))
    btn3.pack(side=side,padx=padx,pady=pady)
    btn4 = Button(fr1, text="{0}".format(displayList[3]), activebackground=abColor, width=width,command=lambda:startExec(btn4["text"]))
    btn4.pack(side=side,padx=padx,pady=pady)
    fr1.pack()
    
def rowNewModules(mainWidget, *displayList, entry):
    fr1=Frame(mainWidget)
    def testing(event):
        print(event)
        mybtn.calculating()
    for i in range(4):
        mybtn=myBtn.myButton(fr1, "{0}".format(displayList[i]),entry)
        mybtn.btn.bind("<Button-1>", testing)
   
    # myBtn.myButton(fr1, "{0}".format(displayList[1]),entry)
    # myBtn.myButton(fr1, "{0}".format(displayList[2]),entry)
    # myBtn.myButton(fr1, "{0}".format(displayList[3]),entry)
    
    fr1.pack()


