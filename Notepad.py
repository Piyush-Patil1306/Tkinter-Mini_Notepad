from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Notepad")
root.geometry("480x650")
root.configure(bg="lightblue")


def clear_text():
    answer = messagebox.askyesno(
    title="Confirmation for clearing text",
    message="Do you want to clear all text?"
)
    if answer == True:
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

format_frame = Frame(root, bg="lightblue")
format_frame.pack(fill=X, pady=5)

is_bold = BooleanVar()


font_style = StringVar()
font_style.set("normal")

def change_font():
    txt.configure(font=("Segoe UI", 14, font_style.get()))

normal_btn = Radiobutton(
    format_frame,
    text="Normal",
    variable=font_style,
    value="normal",
    command=change_font,
    bg="lightblue",
    font=("Segoe UI", 11)
)

bold_btn = Radiobutton(
    format_frame,
    text="Bold",
    variable=font_style,
    value="bold",
    command=change_font,
    bg="lightblue",
    font=("Segoe UI", 11)
)

italic_btn = Radiobutton(
    format_frame,
    text="Italic",
    variable=font_style,
    value="italic",
    command=change_font,
    bg="lightblue",
    font=("Segoe UI", 11)
)

normal_btn.pack(side=LEFT, padx=10)
bold_btn.pack(side=LEFT, padx=10)
italic_btn.pack(side=LEFT, padx=10)

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