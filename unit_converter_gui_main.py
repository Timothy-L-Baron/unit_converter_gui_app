#basic calculator tutorial from codemy.com

from tkinter import *
from tkinter import font
import unit_convert_func_git
import string

#create a window/canvas
root = Tk()

#name the window
root.title('Unit Converter')

num_in = Entry(root, width = 10, borderwidth = 5)
num_in.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
#num_in.insert(0,"quantity")

unit_in = Entry(root, width = 10, borderwidth = 5)
unit_in.grid(row=2, column=1, columnspan=1, padx=10, pady=10)
#unit_in.insert(0,"input unit")

unit_out = Entry(root, width = 10, borderwidth = 5)
unit_out.grid(row=2, column=2, columnspan=1, padx=10, pady=10)
#unit_out.insert(0,"output unit")

#create the functions
def button_click(num):
    global fin
    current = num_in.get()
    num_in.delete(0, END)
    fin = str(current) + str (num)
    num_in.insert(0, str(current) + str(num))
    #print(fin)

def clear_button():
    num_in.delete(0, END)
    unit_in.delete(0, END)
    unit_out.delete(0, END)
    #convert_label.delete(0, END)
    #if convert_label > 0:
        #convert_label.grid_forget()
    #if convert_label

    try:
        convert_label.grid_forget()
    except:
        quit()

def deposit_input_unit(unit):
    global current_in
    current_in = unit_in.get()
    unit_in.delete(0, END)
    current_in = str(unit)
    unit_in.insert(0, unit)
    #print(current_in)

def deposit_output_unit(unit):
    global current_out
    current_out = unit_out.get()
    unit_out.delete(0, END)
    current_out = str(unit)
    unit_out.insert(0, unit)
    #print(curren_out)

def convert(final_answer):
    global convert_label
    #convert_label.grid_forget()
    #convert_label.config(text="")
    #convert_label = Label(root, text="")
    #convert_label.grid(row=10, column=0, columnspan=3)
    #convert_label = Label(root, text="")
    #print(final_answer)
    fin_text = final_answer
    convert_label = Label(root, text=fin_text)
    convert_label.grid(row=10, column=0, columnspan=3)
    #convert_label=Label(root, text="test")
    #convert_label.grid(row=10, column=0, columnspan=3)

#Define the buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_pounds_kg = Button(root, text='pounds to kg', padx=8, pady=20, highlightbackground='orange', font = ("Helvetica", 15, 'bold'), command=lambda: [deposit_input_unit('pounds'), deposit_output_unit('kilograms')] )
button_inches_cm = Button(root, text='inches to cm', padx=10, pady=20, highlightbackground='orange',font =  ("Helvetica", 15, 'bold'), command=lambda: [deposit_input_unit('inches'), deposit_output_unit('centimeters')])
button_feet_meters = Button(root, text='feet to meters', padx=7, pady=20, highlightbackground='orange', font = ("Helvetica", 15, 'bold'), command=lambda: [deposit_input_unit('feet'), deposit_output_unit('meters')])


button_kg_pounds = Button(root, text='kg to pounds', padx=8, pady=20, highlightbackground='orange', font = ("Helvetica", 15, 'bold'), command=lambda: [deposit_input_unit('kilograms'), deposit_output_unit('pounds')])
button_cm_inches = Button(root, text='cm to inches', padx=10, pady=20, highlightbackground='orange', font = ("Helvetica", 15, 'bold'), command=lambda: [deposit_input_unit('centimeters'), deposit_output_unit('inches')])
button_meters_feet = Button(root, text='meters to feet', padx=6, pady=20, highlightbackground='orange', font = ("Helvetica", 15, 'bold'), command=lambda: [deposit_input_unit('meters'), deposit_output_unit('feet')])

button_convert = Button(root, text='convert', padx=54, highlightbackground='green', fg = 'black', font = ("Helvetica", 35), pady=5, command=lambda: convert(unit_convert_func_git.unit_converter(fin, current_in, current_out))) #original xpad=146
button_clear = Button(root, text='clear', padx=73, highlightbackground='red', fg = 'black', font = ("Helvetica", 35), pady=5, command=clear_button)

button_above_inputs = Button(root, text='Unit Converter', padx=146, fg = 'black', font = ("Helvetica", 35, 'bold'), pady=5, command=button_clear,highlightbackground='white', width =10, height = 1)
button_info_inputs = Button(root, text='       quantity                  input unit                output unit     ', padx=187, fg = 'black', font = ("Helvetica", 20, 'bold'),
pady=5, command=button_clear,highlightbackground='white', width =10, height = 1)
button_bottom = Button(root, text='', padx=146, fg = 'white', font = ("Helvetica", 35), pady=10, command=button_clear,highlightbackground='white', width =10, height = 1)


#Place the buttons on the grid
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_pounds_kg.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_kg_pounds.grid(row=6, column=2)

button_inches_cm.grid(row=7, column=0)
button_feet_meters.grid(row=8, column=0)
button_cm_inches.grid(row=7, column=2)
button_meters_feet.grid(row=8, column=2)

button_above_inputs.grid(row=0, column=0, columnspan=3)
button_info_inputs.grid(row=1, column=0, columnspan=3)

button_clear.grid(row=8, column=1, columnspan=1)
button_convert.grid(row=7, column=1, columnspan=1)
button_bottom.grid(row=11, column=0, columnspan=3)




#keep loop running
root.mainloop()
