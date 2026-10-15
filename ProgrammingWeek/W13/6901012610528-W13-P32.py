# code run in Thonny Python 3.14.4
# W13 : Create a Window
import tkinter

window = tkinter.Tk() # create main window
window.title("My tk App") # set title
window.geometry("500x500") # set size

label = tkinter.Label(window, text="Hello")
label.pack(pady=20)

entry1 = tkinter.Entry(window)
entry1.pack(pady=20)

entry2 = tkinter.Entry(window)
entry2.pack()

def multiply():
    num1 = float( entry1.get() )
    num2 = float( entry2.get() )
    result = num1 * num2
    label.config( text=result )

button = tkinter.Button(window, text="Multiply", command=multiply)
button.pack(pady=40)

window.mainloop()
