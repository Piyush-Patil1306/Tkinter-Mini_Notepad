from tkinter import *

root = Tk()
root.title("Notepad")
root.geometry("480x650")
root.configure(bg="lightblue")


def clear_text():
    txt.delete("1.0", END)
    txt.focus_set() #types into box without mouse hover and click

label1 = Label(
    root,
    text="📝 Mini Notepad",
    bg="#2563EB",
    fg="white",
    font=("Segoe UI", 20, "bold"),
    pady=10
)
label1.pack(fill="x")


button_frame = Frame(root, bg="lightblue")
button_frame.pack(side=BOTTOM, fill=X, pady=15)

clearbtn = Button(
    button_frame,
    text="Clear",
    font=("Segoe UI", 12),
    width=15,
    command=clear_text 
)
clearbtn.pack()


txt = Text(
    root,
    font=("Segoe UI", 14)
)
txt.pack(
    fill=BOTH,
    expand=True,
    padx=10,
    pady=10
)

root.mainloop()