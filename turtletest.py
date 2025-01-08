import tkinter as tk

window = tk.Tk()
clickCount = 0

def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="seriously? Do.Not. Press. It")
    elif clickCount == 2:
        button.configure(text="Gah! next time no more button")
    else:
        button.pack_forget()

button = tk.Button(window, text="do not press this button", width=40)
button.bind("<ButtonRelease-1>", onClick)
button.pack(padx=10, pady=10)

window.mainloop()




