from tkinter import *
root=Tk()
e=Entry(root,bg="black",fg="white",bd=6,font=30,justify="right")
e.grid(row=0,column=0,columnspan=4,rowspan=3)

def click(num):
    if(e.get()=='+'or e.get()=='-' or e.get()=='*' or e.get()=='/'):
        e.delete(0,END)
    e.insert(END,str(num))

def operation(char):
    global f_num
    global f_char
    f_num=int(e.get())
    f_char=char
    e.delete(0,END)
    e.insert(0,char)

def equal():
    number=int(e.get())
    e.delete(0,END)
    print(f"{f_num}{f_char}{number}")
    if(f_char=='+'):
        result=f_num+number
    elif(f_char=='-'):
        result=f_num-number
    elif(f_char=='*'):
        result=f_num*number
    else:
        result=f_num/number
    print(result)
    e.insert(0,result)
def clear():
    e.delete(0,END)


button_8=Button(root,text="8",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(8))
button_7=Button(root,text="7",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(7))
button_9=Button(root,text="9",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(9))
button_4=Button(root,text="4",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(4))
button_5=Button(root,text="5",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(5))
button_6=Button(root,text="6",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(6))
button_1=Button(root,text="1",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(1))
button_2=Button(root,text="2",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(2))
button_3=Button(root,text="3",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(3))
button_0=Button(root,text="0",height=3,width=5,bg="black",fg="white",bd=4,command=lambda: click(0))
button_add=Button(root,text="+",height=3,width=5,bg="black",fg="orange",bd=4,command=lambda: operation('+'))
button_sub=Button(root,text="-",height=3,width=5,bg="black",fg="orange",bd=4,command=lambda: operation('-'))
button_mul=Button(root,text="x",height=3,width=5,bg="black",fg="orange",bd=4,command=lambda: operation('*'))
button_div=Button(root,text="/",height=3,width=5,bg="black",fg="orange",bd=4,command=lambda: operation('/'))
button_equalsto=Button(root,text="=",height=3,width=5,bg="black",fg="orange",bd=4,command=equal)
button_clear=Button(root,text="clr",height=3,width=5,bg="black",fg="orange",bd=4,command=clear)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_0.grid(row=6,column=1)
button_add.grid(row=3,column=3)
button_sub.grid(row=4,column=3)
button_mul.grid(row=5,column=3)
button_div.grid(row=6,column=3)
button_equalsto.grid(row=6,column=2)
button_clear.grid(row=6,column=0)


root.mainloop()