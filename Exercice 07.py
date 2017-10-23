from tkinter import *

window = Tk()

def kg_to_brit():
    #convert to pound and return value
    pound=float(e1_value.get())*2.20462
    t1.insert(END,pound)
    #convert to ounce and return value
    ounce=float(e1_value.get())*35.274
    t2.insert(END,ounce)
    #convert to stone and return value
    stone=float(e1_value.get())*0.157473
    t3.insert(END,stone)

l0=Label(window,text="Enter Kilo:")
l0.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=kg_to_brit)
b1.grid(row=0,column=2)

l1=Label(window,text="Pound")
l1.grid(row=1,column=0)

t1=Text(window,height=1,width=10)
t1.grid(row=2,column=0)

l2=Label(window,text="Ounce")
l2.grid(row=1,column=1)

t2=Text(window,height=1,width=10)
t2.grid(row=2,column=1)

l3=Label(window,text="Stone")
l3.grid(row=1,column=2)

t3=Text(window,height=1,width=10)
t3.grid(row=2,column=2)

window.mainloop()
