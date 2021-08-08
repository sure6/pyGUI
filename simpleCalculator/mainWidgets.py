'''
Created on 2021年4月21日

@author: leesure
'''
from tkinter import Tk, Label, Button, Entry, Frame,StringVar
from tkinter.constants import LEFT
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox

root = Tk()
root.geometry("400x100+500+300")
root.title("Simple Calculator v1.0.0")
root.resizable(0,0)

varStr1 = StringVar()
varStr2= StringVar()
varStr3= StringVar()
calcuSymbol=StringVar()
varStr3.set("?")

def howManytBitpoint(number1,number2, symbol=None):
    if isinstance(number1, float) :
        newStr1= str(number1)[ str(number1).find(".")+1:]
    else:
        newStr1=""
        
    if isinstance(number2, float):
        newStr2= str(number2)[ str(number2).find(".")+1:]
    else:
        newStr2=""
        
    if symbol=="x":   
        return len(newStr1)+len(newStr2)
    
    if  len(newStr1) > len(newStr2): 
        return  len(newStr1) 
    else: 
        return len(newStr2)
    
 
    
    
def gInt(number):
    if isinstance(number, float) and str(number)[-1]=="0" :
        return int(number)
    else:
        return number

def calculating():
    if len(varStr1.get()) >9 or len(varStr2.get())>9:
        showinfo("error", "Input value is out of range")
        varStr1.set("")
        varStr2.set("")
        varStr3.set("?")
        return 
    
    if varStr1.get()=="" or varStr2.get()=="":
        showinfo("error", "Input value is not none")
        varStr1.set("")
        varStr2.set("")
        varStr3.set("?")
        return 
    else:
        try:
            num1=eval(varStr1.get())
            num2=eval(varStr2.get())
        except:
            showinfo("error", "Input value is not letter or other symbols")
            return 
        else:
            if calcuSymbol.get() =="+":
                num3=num1+num2
                varStr3.set(round(gInt(num3),howManytBitpoint(num1, num2)))
            elif calcuSymbol.get() =="-":
                num3=num1-num2
                varStr3.set(round(gInt(num3),howManytBitpoint(num1, num2)))
            elif calcuSymbol.get() =="x":
                num3=num1*num2
                varStr3.set(gInt(num3))
            elif calcuSymbol.get() =="/":
                if num2==0:
                    showinfo("error", "The divisor cannot be 0")
                    varStr2.set("")
                    varStr3.set("?")
                    return
                else:
                    num3=num1/num2
                    varStr3.set(gInt(num3))
                    
            # print(howManytBitpoint(num2))
            print(round(num3,howManytBitpoint(num1, num2)))
            print(num3)
            # varStr3.set(round(gInt(num3),howManytBitpoint(num1, num2)))
            
fr=Frame()

ent1= Entry(fr, width="9",textvariable=varStr1)
ent1.pack(side=LEFT,padx=5,pady=5)

# label1=Label(fr, text="+")
# label1.pack(side=LEFT,padx=5,pady=5)
com=Combobox(fr,width="3", textvariable=calcuSymbol,state= "readonly")
com.pack(side=LEFT,padx=5,pady=5)
com["value"]=("+","-","x","/")
com.current(0)


ent2= Entry(fr, width="9",textvariable=varStr2)
ent2.pack(side=LEFT,padx=5,pady=5)

label2=Label(fr, text="=")
label2.pack(side=LEFT,padx=5,pady=5)

label3=Label(fr, textvariable=varStr3)
label3.pack(side=LEFT,padx=5,pady=5)

fr.pack()

btn=Button(root,text="calculate", command=calculating, activebackground="red")
btn.pack(padx=5,pady=5)

if __name__=="__main__":    
    root.mainloop()