from tkinter import *
import tkinter as tk


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), Surgery.get()))


master = tk.Tk()

v = tk.IntVar()

tk.Label(master,
         text="""Choose a 
programming language:""",
         justify=tk.LEFT,
         padx=20).pack()
tk.Radiobutton(master,
               text="Python",
               padx=20,
               variable=v,
               value=1).pack(anchor=tk.W)
tk.Radiobutton(master,
               text="Perl",
               padx=20,
               variable=v,
               value=2).pack(anchor=tk.W)

tk.Label(master, text="Age").grid(row=0)
tk.Label(master, text="Surgery").grid(row=1)
tk.Label(master, text="Doctor visits").grid(row=2)
tk.Label(master, text="Allergy").grid(row=3)
tk.Label(master, text="Medication").grid(row=4)
tk.Label(master, text="Disease").grid(row=5)
tk.Label(master, text="Bmi").grid(row=6)
tk.Label(master, text="Value risk").grid(row=7)

Age = tk.Entry(master)
Surgery = tk.Entry(master)
doc_visits = tk.Entry(master)
Allergy = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)

Age.grid(row=0, column=1)
Surgery.grid(row=1, column=1)
doc_visits.grid(row=2, column=1)
Allergy.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=8,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Eligible', command=show_entry_fields).grid(row=8,
                                                           column=1,
                                                           sticky=tk.W,
                                                           pady=4)

master.mainloop()
