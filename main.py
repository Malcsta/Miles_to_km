import tkinter as tk
from tkinter import ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.60934
    output_string.set(km_output)

# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

# title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Aptos 22 bold')
title_label.pack()

# input field 
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack()
input_frame.pack(pady =  10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                          text = 'Output', 
                          font = 'aptos 16', 
                          textvariable = output_string)
output_label.pack(pady = 10)

# run 
window.mainloop()
