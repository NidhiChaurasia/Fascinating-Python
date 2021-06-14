from tkinter import *
root = Tk()
root.geometry("600x600")

def getvals():
    print("Your form has been Submitted")

Label(root, text="Python Registration Form",font="times 15 bold").grid(row=0,column=3)

Name = Label(root, text = "Name")
Name.grid(row=1 ,column=2)
Phone = Label(root, text = "Phone")
Phone.grid(row=2, column=2)
Gender = Label(root, text = "Gender")
Gender.grid(row=3, column=2)
Country = Label(root, text = "Country")
Country.grid(row=4, column=2)
Payment_Mode = Label(root, text = "Payment_mode")
Payment_Mode.grid(row=5 ,column=2)
Address = Label(root, text="Address")
Address.grid(row=6 ,column=2)

Name_value = StringVar
Phone_value = StringVar
Gender_value = StringVar
Country_value = StringVar
Payment_Mode_value = StringVar
Address_value = StringVar
checkvalue = IntVar

Name_entry = Entry(root, textvariable = Name_value)
Name_entry.grid(row=1, column=3)
Phone_entry = Entry(root, textvariable = Phone_value)
Phone_entry.grid(row=2, column=3)
Gender_value = Entry(root, textvariable = Gender_value)
Gender_value.grid(row=3, column=3)
Country_value = Entry(root, textvariable = Country_value)
Country_value.grid(row=4, column=3)
Payment_Mode_value = Entry(root, textvariable = Payment_Mode_value)
Payment_Mode_value.grid(row=5, column=3)
Address_value = Entry(root, textvariable = Address_value)
Address_value.grid(row=6, column=3)

Check_btn = Checkbutton(text="Remember me?",variable=checkvalue)
Check_btn.grid(row=7, column=3)

Button(text="Submit", command=getvals).grid(row=8, column=3)


root.mainloop()
