import tkinter as tk
from tkinter import ttk

def convert():
	denary_input = entry_int.get()
	binary_output = bin(denary_input) 
	output_string.set(binary_output[2: ])

window = tk.Tk()
window.title("Binary Converter")
window.geometry("300x150")

title_label = ttk.Label(master = window, text = "Binary Converter", font = "bold")
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

output_string = tk.StringVar()
output_label = ttk.Label(
	master = window,
	text = "Output",
	textvariable = output_string)

output_label.pack(pady = 5)

window.mainloop()