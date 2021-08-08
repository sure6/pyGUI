"%","0","=","/"'''
Created on 2021年4月20日

@author: leesure
'''
from tkinter import Tk, Label, Button, Entry, Frame,StringVar
from tkinter.constants import LEFT
from calculator import tools
from calculator import myBtn

root = Tk()
root.geometry("280x200+600+200")
root.title("Simple Calculator v1.0.0")

# txtlable=Label(root,text="hello, this is a Calculator", bg="red", fg="yellow", font="Arial 12 italic" )
# txtlable.pack()
varStr = StringVar()
# varStr.set("33")
# varStr.set("4")
ent1= Entry(root, width="30", textvariable=varStr)
ent1.pack(padx=5,pady=5)

# def testing():  
#     varStr.set(2)    
#     ent1["textvariable"]=varStr.get()
#
# btn1 = Button(root, text="2",  command=testing)
# btn1.pack()

tools.rowNewModules(root,"1","2","3","+",entry=ent1)
tools.rowNewModules(root,"4","5","6","-",entry=ent1)
tools.rowNewModules(root,"7","8","9","x",entry=ent1)
tools.rowNewModules(root,"%","0","=","/",entry=ent1)

# tools.rowModules(root,"1","2","3","+",abColor="red",width="5",side=LEFT,padx=5,pady=5)
# tools.rowModules(root,"4","5","6","-",abColor="red",width="5",side=LEFT,padx=5,pady=5)
# tools.rowModules(root,"7","8","9","x",abColor="red",width="5",side=LEFT,padx=5,pady=5)
# tools.rowModules(root,"%","0","=","/",abColor="red",width="5",side=LEFT,padx=5,pady=5)

if __name__=="__main__":    
    root.mainloop()