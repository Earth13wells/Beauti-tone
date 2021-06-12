"""-------------------------------------------------------------|
|           This code was written by Gabriel Presley            |
|               This code is licensed under the                 |
|                  GNU GENERAL PUBLIC LICENSE                   |
|                    Version 3, 29 June 2007                    |
|  This software was not originally created for any one entity  |
|This software has no ties to HomeHardware or Beauti-tone brands|
|            any perceived relation is not intended.            |
--------------------------------------------------------------"""
try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk

# Defining the main window
first = tk.Tk()
first.title('Formula Converter')

# Old lables headers
tk.Label(first, text="Ounces:").grid(row=0, column=0)
tk.Label(first, text="Shots:").grid(row=0, column=1)
tk.Label(first, text="1/2 Shots:").grid(row=0, column=2)
tk.Label(first, text="1/4 Shots:").grid(row=0, column=3)

#
# Conversion function
def convert():
    for z in range(0, 7):
        New_Ounces[z].config(text=Old_Ounces[z].get())
        New_Shots[z].config(text=Old_Shots[z].get())

        if(Old_Quarters[z].get() == ""):
            Old_Quarters[z].insert(0, "0")
        if(Old_Halfs[z].get() == ""):
            Old_Halfs[z].insert(0, "0")

        try:
            Sixteenths = (int(Old_Quarters[z].get())*4 + int(Old_Halfs[z].get())*8)
            if(Sixteenths >= 17):
                tk.Label(first, text="TOO MANY FRACTIONAL SHOTS").grid(row=8, column=4)
            New_Sixteenths[z].config(text=Sixteenths)
        except ValueError:
            tk.Label(first, text="INVALID INPUT").grid(row=8, column=4)


# clear function
def clear():
    for p in range(0, 7):
        Old_Ounces[p].delete(0, 100)
        Old_Shots[p].delete(0, 100)
        Old_Halfs[p].delete(0, 100)
        Old_Quarters[p].delete(0, 100)


#  Defining some empty arrays to fill with layout
Old_Ounces = [[]]*7
Old_Shots = [[]]*7
Old_Halfs = [[]]*7
Old_Quarters = [[]]*7

# Filling arrays with layout
for i in range(0, 7):
    Old_Ounces[i] = tk.Entry(first)
    Old_Shots[i] = tk.Entry(first)
    Old_Halfs[i] = tk.Entry(first)
    Old_Quarters[i] = tk.Entry(first)

    Old_Ounces[i].grid(row=i+1, column=0)
    Old_Shots[i].grid(row=i+1, column=1)
    Old_Halfs[i].grid(row=i+1, column=2)
    Old_Quarters[i].grid(row=i+1, column=3)

#  Convert_button
convert_button = tk.Button(first, text="Convert", command=convert)
convert_button.grid(row=i+1, column=4)

#  clear_button
clear_button = tk.Button(first, text="Clear", command=clear)
clear_button.grid(row=i, column=4)

# new lables titles
tk.Label(first, text="Ounces:").grid(row=0, column=5)
tk.Label(first, text="Shots:").grid(row=0, column=6)
tk.Label(first, text="1/16 Shots:").grid(row=0, column=7)

#  Defining some empty arrays to fill with layout
New_Ounces = [[]]*7
New_Shots = [[]]*7
New_Sixteenths = [[]]*7

#  Filling arrays with layout
first.grid_columnconfigure(1, weight=1)

for i in range(0, 7):
    New_Ounces[i] = tk.Entry(first)
    New_Shots[i] = tk.Entry(first)
    New_Sixteenths[i] = tk.Entry(first)

    New_Ounces[i] = tk.Label(first, text="", font='size, 10')
    New_Shots[i] = tk.Label(first, text="", font='size, 10')
    New_Sixteenths[i] = tk.Label(first, text="", font='size, 10')

    New_Ounces[i].grid(row=i+1, column=5)
    New_Shots[i].grid(row=i+1, column=6)
    New_Sixteenths[i].grid(row=i+1, column=7)

first.mainloop()
