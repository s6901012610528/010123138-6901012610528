# code run in Thonny Python 3.14.4
# W11 : Tkinter
import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_oval(200, 50, 400, 250, fill="orange")
canvas.create_line(300, 250, 300, 450)

root.mainloop()