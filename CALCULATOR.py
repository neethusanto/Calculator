import parser
from  tkinter import  *
root=Tk()

root.configure(bg="light green")

root.title("Calculator")
display=Entry(root)
display.grid(row=1,columnspan=5,sticky=W+E)

i=0
def get_variable(num):
    global  i
    display.insert(i,num)
    i+=1

def clearall():
    display.delete(0,END)

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clearall()
        display.insert(0,new_string)
    else:
        clearall()
        display.insert(0,"Error")

def get_operator(opr):
    global  i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()
        display.insert(0,"Error")


Button(root,text="7",bg="red",fg="black",command=lambda :get_variable(7),height=2, width=8).grid(row=3,column=0)
Button(root,text="8",bg="red",fg="black",command=lambda :get_variable(8),height=2, width=8).grid(row=3,column=1)
Button(root,text="9",bg="red",fg="black",command=lambda :get_variable(9),height=2, width=8).grid(row=3,column=2)
Button(root,text="4",bg="red",fg="black",command=lambda :get_variable(4),height=2, width=8).grid(row=4,column=0)
Button(root,text="5",bg="red",fg="black",command=lambda :get_variable(5),height=2, width=8).grid(row=4,column=1)
Button(root,text="6",bg="red",fg="black",command=lambda :get_variable(6),height=2, width=8).grid(row=4,column=2)
Button(root,text="3",bg="red",fg="black",command=lambda :get_variable(3),height=2, width=8).grid(row=5,column=2)
Button(root,text="2",bg="red",fg="black",command=lambda :get_variable(2),height=2, width=8).grid(row=5,column=1)
Button(root,text="1",bg="red",fg="black",command=lambda :get_variable(1),height=2, width=8).grid(row=5,column=0)
Button(root,text="0",bg="red",fg="black",command=lambda :get_variable(0),height=2, width=8).grid(row=6,column=1)
Button(root,text="^2",bg="red",fg="black",command=lambda :get_variable('**2'),height=2, width=8).grid(row=6,column=0)

Button(root,text="C",bg="red",fg="black",command=lambda :clearall(),height=2, width=8).grid(row=2,column=0)
Button(root,text="%",bg="red",fg="black",command=lambda :get_operator('%'),height=2, width=8).grid(row=2,column=1)
Button(root,text="<-",bg="red",fg="black",command=lambda:undo(),height=2, width=8).grid(row=2,column=2)
Button(root,text="/",bg="red",fg="black",command=lambda :get_operator('/'),height=2, width=8).grid(row=2,column=3)
Button(root,text="*",bg="red",fg="black",command=lambda :get_operator('*'),height=2, width=8).grid(row=3,column=3)
Button(root,text="-",bg="red",fg="black",command=lambda :get_operator('-'),height=2, width=8).grid(row=4,column=3)
Button(root,text="+",bg="red",fg="black",command=lambda :get_operator('+'),height=2, width=8).grid(row=5,column=3)
Button(root,text=".",bg="red",fg="black",command=lambda :get_operator('.'),height=2, width=8).grid(row=6,column=2)
Button(root,text="=",bg="black",fg="blue",command=lambda :calculate(),height=2, width=8).grid(row=6,column=3)

root.mainloop()