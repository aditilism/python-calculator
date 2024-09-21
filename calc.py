import tkinter as tk

# Function to handle button clicks
def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input screen
def clear_screen():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))  # 'eval' evaluates the string as a Python expression
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Initialize the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
window.resizable(0, 0)

expression = ""
input_text = tk.StringVar()

# Create the display screen
input_frame = tk.Frame(window, width=400, height=50, bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # 'ipady' is internal padding to increase height of the entry widget

# Create the frame for buttons
btns_frame = tk.Frame(window, width=500, height=500 )
btns_frame.pack()

# First row
clear = tk.Button(btns_frame, text="Calc", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=clear_screen).grid(row=0, column=0, columnspan=5)
divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button("/")).grid(row=4, column=3)

# Second row
seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(7)).grid(row=1, column=0)
eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(8)).grid(row=1, column=1)
nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(9)).grid(row=1, column=2)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button("*")).grid(row=1, column=3)

# Third row
four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(4)).grid(row=2, column=0)
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(5)).grid(row=2, column=1)
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(6)).grid(row=2, column=2)
sub = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button("-")).grid(row=2, column=3)

# Fourth row
one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(1)).grid(row=3, column=0)
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(2)).grid(row=3, column=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(3)).grid(row=3, column=2)
add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button("+")).grid(row=3, column=3)

# Fifth row
zero = tk.Button(btns_frame, text="0", fg="black", width=22, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(0)).grid(row=4, column=0, columnspan=2)
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: click_button(".")).grid(row=4, column=2)
equals = tk.Button(btns_frame, text="=", fg="black", width=43, height=3, bd=2, bg="#fff", cursor="hand2", command=evaluate).grid(row=5,column=0,columnspan=4)

# Run the main loop
window.mainloop()
