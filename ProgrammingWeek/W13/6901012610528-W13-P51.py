# code run in Thonny Python 3.14.4
# W13 : Add a Frame
import tkinter

window = tkinter.Tk() # create main window
window.title("My tk App") # set title
window.geometry("500x500") # set size

label = tkinter.Label(window, text="Hello")
label.pack(pady=20)

entry_frame = tkinter.Frame(window)
entry_frame.pack(pady=20)

entry1 = tkinter.Entry(entry_frame, width=10)
entry1.pack(side="left", padx=5)

entry2 = tkinter.Entry(entry_frame, width=10)
entry2.pack(side="left", padx=5)

def multiply():
    num1 = float( entry1.get() )
    num2 = float( entry2.get() )
    result = num1 * num2
    label.config( text=result )

button = tkinter.Button(window, text="Multiply", command=multiply)
button.pack(pady=40)

window.mainloop()
