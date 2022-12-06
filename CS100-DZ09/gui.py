import tkinter as tk
from tkinter import ttk 

def pozovi():
    print(text.get())

def stam(txt):
    print(txt.get())

fields = {}

root = tk.Tk()
root.title("Petar - center")
root.resizable(False, False)
# root.iconbitmap("")
tk.Label(root, text = "Test").pack()
ttk.Label(root, text='Themed Label').pack()
ttk.Button(root, text="Uvezi", command=pozovi).pack(ipadx=10, ipady=10, anchor=tk.W, padx=20, pady=20)
text = tk.StringVar()

fields['username'] = tk.Label(root, text = "Username")
fields['usernameInput'] = ttk.Entry(root, textvariable=text)
fields['password'] = tk.Label(root, text = "Password")
fields['passwordInput'] = ttk.Entry(root, show="*")
fields['login'] = ttk.Button(root, text="Login", command=pozovi)

for field in fields.values():
    field.pack(padx = 3, pady = 3, anchor = tk.W)
root.mainloop()