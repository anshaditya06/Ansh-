# Simple GUI Calculator

import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("320x420")
root.resizable(True, True)

expression = ""

# Update expression
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Evaluate expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Clear screen
def clear():
    global expression
    expression = ""
    input_text.set("")

# Square root
def sqrt():
    global expression
    try:
        expression = str(math.sqrt(float(expression)))
        input_text.set(expression)
    except:
        input_text.set("Error")
        expression = ""

# Input field
input_text = tk.StringVar()
input_frame = tk.Frame(root, width=320, height=60)
input_frame.pack()

input_field = tk.Entry(
    input_frame,
    font=('arial', 20),
    textvariable=input_text,
    justify='right'
)
input_field.pack(ipady=10, fill='both')

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0

for btn in buttons:
    if btn == '=':
        action = equal
    else:
        action = lambda x=btn: press(x)

    tk.Button(
        btn_frame,
        text=btn,
        width=4,
        height=2,
        command=action
    ).grid(row=row, column=col)

    col += 1
    if col == 4:
        row += 1
        col = 0

# Extra buttons
tk.Button(btn_frame, text="C", width=15, height=3, command=clear)\
    .grid(row=5, column=0, columnspan=2)

tk.Button(btn_frame, text="√", width=15, height=3, command=sqrt)\
    .grid(row=5, column=2, columnspan=2)

root.mainloop()
