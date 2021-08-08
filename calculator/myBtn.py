'''
Created on 2021年4月21日

@author: leesure
'''
import tkinter
from tkinter.constants import LEFT
class myButton():
    def __init__(self, frame, text, entry, **kwargs):
        side = kwargs.get('side') if 'side' in kwargs else ()
        self.btn = tkinter.Button(
            frame,
            text = text,
            activeforeground="blue",
            activebackground="pink",
            width="5",
            command=lambda :entry.insert("end", text)
        )
        if side:
            self.btn.grid(row=side[0], column=side[1])
        else:
            self.btn.pack(side=LEFT,padx=5,pady=5)  
        
    def calculating(self):
        if self.btn['text']=="+":
            print("this is a +")
        else:
            print("testing")