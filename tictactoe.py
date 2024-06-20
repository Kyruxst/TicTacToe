import tkinter as tk

root = tk.Tk()
root.title('TicTacToe')
root.geometry('500x500')
root.resizable(height=False, width=False)

baseframe = tk.Frame(root, bg='assets\TictacBackground.png')
baseframe.pack(fill='both', expand=True)


firstbutton = tk.Button(baseframe, text='blah')

root.mainloop()