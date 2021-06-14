from tkinter import *

window = Tk()
window.geometry("800x700")

def calculate():
    paneer_tikka = e1.get()
    fried_rice = e2.get()
    spring_rolls = e3.get()
    chinese_momos = e4.get()
    total = ((int(paneer_tikka)*150)+(int(fried_rice)*120)+(int(spring_rolls)*120)+(int(chinese_momos)*200))
    label12 = Label(window,text=total,font="times 25 bold")
    label12.place(x=200,y=440)
    

label6 = Label(window,text="CHINESE DELIGHT",font="times 30 bold")
label6.place(x=180, y=20)
#------------menu option-------------
label1 = Label(window,text="MENU",font="times 28 bold")
label1.place(x=550,y=70)

label2 = Label(window,text="Paneer Tikka        Rs.150",font="times 18 bold")
label2.place(x=450,y=120)

label3 = Label(window,text="Fried Rice             Rs.120",font="times 18 bold")
label3.place(x=450,y=150)

label4 = Label(window,text="Spring Rolls          Rs.120",font="times 18 bold")
label4.place(x=450,y=180)

label5 = Label(window,text="Chinese Momos    Rs.200",font="times 18 bold")
label5.place(x=450,y=210)

label7 = Label(window,text="Select the items",font="times 20 bold")
label7.place(x=80, y=90)

label8 = Label(window,text="Paneer Tikka",font="times 18 bold")
label8.place(x=20,y=140)

e1 = Entry(window)
e1.place(x=20,y=180)

label9 = Label(window,text="Fried Rice",font="times 18 bold")
label9.place(x=250,y=140)

e2 = Entry(window)
e2.place(x=250,y=180)

label10 = Label(window,text="Spring Rolls",font="times 18 bold")
label10.place(x=20,y=220)

e3 = Entry(window)
e3.place(x=20,y=250)

label11 = Label(window,text="Chinese Momos",font="times 18 bold")
label11.place(x=250,y=215)

e4 = Entry(window)
e4.place(x=250,y=250)
#Making command for Billing
b2 = Button(window,text="BILL",font="times 20 bold",width=20,command=calculate)
b2.place(x=100,y=350)
window.mainloop()