from cmath import *
import tkinter as tk


def func_calc():
    values = ed_in.get().strip()
    ed_res.delete(0, tk.END)
    ed_res.insert(0, eval(values))


root = tk.Tk()
root.title('Calc')

tk.Label(root, text='Введите выражение:').grid(row=1, column=0)
tk.Label(root, text='=').grid(row=2, column=0)

ed_in = tk.Entry(root, width=60)
ed_in.grid(row=1, column=1)

but = tk.Button(root, text='=', command=func_calc)
but.grid(row=1, column=2)

ed_res = tk.Entry(root, width=60)
ed_res.grid(row=2, column=1)

root.mainloop()



