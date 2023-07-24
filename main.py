
from tkinter import *
import math
def press(num):
  global expression
  expression= expression +str(num)
  equation.set(expression)

def equalpress():
  try:
    global expression 
    total=str(eval(expression))
    equation.set(total)
    expression=""
  except:
    equation.set=("error")
    expression=''


def clear():
  try:
    global expression
    expression=""
    equation.set("")
  except:
    equation.set=("error")
    expression=''
 


if TRUE:
  root=Tk()
  root.title("Calculator App")
  root.geometry("500x500")
  root.configure(bg="cyan")
  expression=''
  equation=StringVar()
  expression_field=Entry(root,textvariable=equation)
  expression_field.grid(columnspan=4,ipadx=70)



button7=Button(root, text="7",bg="white",fg="black",command=lambda: press(7), width=6,height=1)
button7.grid(row=2, column=0)

button8=Button(root,text="8",bg="white",fg="black",command=lambda: press(8),width=6,height=1)
button8.grid(row=2,column=1)

button9=Button(root,text="9",bg="white",fg="black",command=lambda: press(9),width=6,height=1)
button9.grid(row=2,column=2)

equal=Button(root, text="=",bg="white",fg="black",command=lambda: equalpress(),width=7,height=1)

button4=Button(root, text="4",bg="white",fg="black",command=lambda: press(4),width=6,height=1)
button4.grid(row=3, column=0)

button5=Button(root, text="5",bg="white",fg="black",command=lambda: press(5),width=6,height=1)
button5.grid(row=3, column=1)

button6=Button(root, text="6",bg="white",fg="black",command=lambda: press(6),width=6,height=1)
button6.grid(row=3, column=2)

button1=Button(root, text="1",bg="white",fg="black",command=lambda: press(1),width=6,height=1)
button1.grid(row=4, column=0)

button2=Button(root, text="2",bg="white",fg="black",command=lambda: press(2),width=6,height=1)
button2.grid(row=4,column=1)

button3=Button(root, text="3",bg="white",fg="black",command=lambda: press(3),width=6,height=1)
button3.grid(row=4,column=2)

button0=Button(root, text="0",bg="white",fg="black",command=lambda: press(0),width=6,height=1)
button0.grid(row=5,column=0)

plus=Button(root, text=' + ', fg='black',bg='gray77',command=lambda:press("+"),width=6,height=1)
plus.grid(row=5,column=3)

minus=Button(root, text=' - ', fg='black',bg='gray77',command=lambda:press("-"),width=6,height=1)
minus.grid(row=4,column=3)

divide=Button(root, text=' / ', fg='black',bg='gray77',command=lambda:press("/"),width=6,height=1)
divide.grid(row=2,column=3)

multiply=Button(root, text=' * ', fg='black',bg='gray77',command=lambda:press("*"),width=6,height=1)
multiply.grid(row=3,column=3)

equal=Button(root, text=' = ', fg='black',bg='limegreen',command=equalpress,width=6,height=1)
equal.grid(row=5,column=2)

decimal=Button(root,text=' . ', fg='black', bg='white', command=lambda:press("."),width=6,height=1)
decimal.grid(row=5,column=1)

clear=Button(root, text='clear', fg='black',bg='tomato',command=clear,width=6,height=1)
clear.grid(row=6,column=2)

modulus=Button(root, text=' % ', fg='black',bg='gray77',command=lambda:press('%')
,width=6,height=1)
modulus.grid(row=6,column=0)

exp=Button(root, text=' ^ ', fg='black',bg='gray77',command=lambda:press("**"),
width=6,height=1)
exp.grid(row=6,column=1)


root.mainloop()