import tkinter as tk
from tkinter.constants import X

window = tk.Tk()
window.title("KBBI Apps")

frm_entry = tk.Frame(master=window)
ent_keyword = tk.Entry(master=frm_entry, width=X)
label_keyword = tk.Label(master=frm_entry, text="Cari Kata")

btn_search = tk.Button(
    master= window,
    text="Submit"
)

window.mainloop()
