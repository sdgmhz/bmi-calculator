import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.title("BMI Calculator by sdgmhz")

lbl_weight = ttk.Label(
    master=window,
    text="Weight (Kg):",
)

ent_weight = ttk.Entry(
    master=window,
    # width=40,
)

lbl_height = ttk.Label(
    master=window,
    text="Height (cm):",
)

ent_height = ttk.Entry(
    master=window,
)

def bmi_analysis(bmi):
    if bmi < 18.5 :
        return 'underweight range!'
    if bmi <= 24.9:
        return 'healthy weight range!'
    if bmi <= 29.9:
        return 'overweight range!'
    if bmi <= 34.9:
        return 'obese range class I !!'
    if bmi <= 39.9:
        return 'obese range class II !!'
    if bmi >= 40:
        return 'obese range class III !!!'

def calc_bmi(*args):
    try:
        if float(ent_weight.get()) <= 0:
            lbl_result['text'] = 'Wight should be a positive number!'
        elif float(ent_height.get()) <= 0:
            lbl_result['text'] = 'Height should be a positive number!'
        else:
            bmi = f'{(float(ent_weight.get()))/(float(ent_height.get())/100)**2: 0.2f}'
            lbl_result['text'] = f'Your BMI is : {bmi} and you are in :\n        {bmi_analysis(float(bmi))}'
    except ValueError:
        if ent_weight.get() == '':
            lbl_result['text'] = 'Wight field is empty!'
        
        elif ent_height.get() == '':
            lbl_result['text'] = 'Height field is empty!'
        else:
            lbl_result['text'] = 'You should enter numbers in both fields'

window.bind('<Return>', calc_bmi)

btn_calc = ttk.Button(
    master=window,
    text="Calculate BMI",
    width= 40,
    command=calc_bmi,
)

lbl_result = ttk.Label(
    master=window,
)

lbl_weight.grid(row=0, column=0, padx=10, pady=10)
ent_weight.grid(row=0, column=1,padx=5, pady=10)
lbl_height.grid(row=0, column=2,padx=10, pady=10)
ent_height.grid(row=0, column=3, padx=5, pady=10)
btn_calc.grid(row=1, column=1, columnspan=3, pady=10)
lbl_result.grid(row=2, column=1, columnspan=3, pady=20,)


window.mainloop()