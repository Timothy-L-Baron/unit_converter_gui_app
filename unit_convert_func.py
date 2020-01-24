#unit converter functions
from tkinter import *

#create a list of aceptabl eunit values
unit_vals = ['inches', 'feet', 'centimeters', 'meters', 'pounds', 'grams', 'kilograms']

#create a dictionary of unit conversion values
unit_dic = {'inches_to_centimeters' : 2.54, 'centimeters_to_inches' : 1/2.54, 'feet_to_inches' : 12, 'inches_to_feet' : 1/12, 'meters_to_inches' : 39.9071, 'inches_to_meters' : 1/39.9071,
'feet_to_centimeters' : 30.48, 'centimeters_to_feet' : 1/30.48, 'meters_to_centimeters' : 100, 'centimeters_to_meters' : 1/100, 'meters_to_feet' : 3.28084, 'feet_to_meters' : 1/3.28084,
'pounds_to_grams' : 453.592, 'grams_to_pounds' : 1/453.592, 'kilograms_to_pounds' : 2.20462, 'pounds_to_kilograms' : 1/2.20462, 'kilograms_to_grams' : 1000, 'gram_to_kilograms' : 1/1000,
'feet_to_feet' : 1, 'inches_to_inches' : 1, 'centimeters_to_centimeters' : 1, 'meters_to_meters' : 1, 'pound_to_pound' : 1, 'grams_to_grams' : 1, 'kilograms_to_kilograms' : 1}

#create dictionary of single unit values
single_unit_dic = {'inches' : 'inch', 'feet' : 'foot', 'centimeters' : 'centimeter', 'meters' : 'meter', 'pounds' : 'pound', 'grams' : 'gram', 'kilograms' : 'kilogram'}

#create a function to do unit conversion that takes three parameters (n_in, u_in, u_out)
def unit_converter(n_in, u_in, u_out):
    #convert n_in to a float
    n_in = float(n_in)
    print(n_in)
    #create an input phrase so that the proper conversion value can be obtained from the unit_dic
    input_phrase = u_in + '_to_' + u_out
    print(input_phrase)
    #calculate fin_out using the input number and conversion value
    fin_out = n_in * unit_dic.get(input_phrase)
    #change units to singular string for output if number in front of unit is 1
    if n_in == 1.0:
        u_in = single_unit_dic.get(u_in)
    if fin_out == 1.0:
        u_out = single_unit_dic.get(u_out)
    #return the conversion
    x = '{} {} is approximately {} {}'.format(n_in, u_in, fin_out, u_out)
    #return print('{} {} is approximately {} {}'.format(n_in, u_in, fin_out, u_out))
    return x

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


def deposit_output_unit(unit):
    global current_out
    current_out = unit_out.get()
    unit_out.delete(0, END)
    current_out = str(unit)
    unit_out.insert(0, unit)
    #print(curren_out)

def convert(final_answer):
    global convert_label
    fin_text = final_answer
    convert_label = Label(root, text=fin_text)
    convert_label.grid(row=10, column=0, columnspan=3)
