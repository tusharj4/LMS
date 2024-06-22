from tkinter import *

# Function to perform arithmetic operations
def calculate():
    try:
        result = eval(entry.get())
        label.config(text = str(result))
    except:
        label.config(text = "Invalid input")

# Create the main window
window = Tk()
window.title("Simple Calculator")

# Create the entry field for user input
entry = Entry(window, width = 35, borderwidth = 5)
entry.grid(row = 0, column = 0, columnspan = 3)

# Create the buttons for arithmetic operations
button_1 = Button(window, text = "1", padx = 40, pady = 20, command = lambda: entry.insert(END, "1"))
button_2 = Button(window, text = "2", padx = 40, pady = 20, command = lambda: entry.insert(END, "2"))
button_3 = Button(window, text = "3", padx = 40, pady = 20, command = lambda: entry.insert(END, "3"))
button_4 = Button(window, text = "4", padx = 40, pady = 20, command = lambda: entry.insert(END, "4"))
button_5 = Button(window, text = "5", padx = 40, pady = 20, command = lambda: entry.insert(END, "5"))
button_6 = Button(window, text = "6", padx = 40, pady = 20, command = lambda: entry.insert(END, "6"))
button_7 = Button(window, text = "7", padx = 40, pady = 20, command = lambda: entry.insert(END, "7"))
button_8 = Button(window, text = "8", padx = 40, pady = 20, command = lambda: entry.insert(END, "8"))
button_9 = Button(window, text = "9", padx = 40, pady = 20, command = lambda: entry.insert(END, "9"))
button_0 = Button(window, text = "0", padx = 40, pady = 20, command = lambda: entry.insert(END, "0"))

button_add = Button(window, text = "+", padx = 40, pady = 20, command = lambda: entry.insert(END, "+"))
button_subtract = Button(window, text = "-", padx = 40, pady = 20, command = lambda: entry.insert(END, "-"))
button_multiply = Button(window, text = "*", padx = 40, pady = 20, command = lambda: entry.insert(END, "*"))
button_divide = Button(window, text = "/", padx = 40, pady = 20, command = lambda: entry.insert(END, "/"))

button_equals = Button(window, text = "=", padx = 40, pady = 20, command = calculate)

# Place the buttons on the window
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)

button_add.grid(row = 4, column = 1)
button_subtract.grid(row = 4, column = 2)

button_multiply.grid(row = 5, column = 0)
button_divide.grid(row = 5, column = 1)

button_equals.grid(row = 5, column = 2)

# Create a label to display the result
label = Label(window, text = "")
label.grid(row = 6, column = 0, columnspan = 3)

# Start the main loop
window.mainloop()
