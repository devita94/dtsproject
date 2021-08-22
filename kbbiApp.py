import tkinter as tk
from tkinter.constants import X

window = tk.Tk()
window.title("KBBI Apps")

frm_entry = tk.Frame(master=window)
ent_keyword = tk.Entry(master=frm_entry, width=X)
label_keyword = tk.Label(master=frm_entry, text="Cari Kata")

def find_word():
    worddict = {
        "ayah" : "orang tua kandung laki-laki; bapak",
        "ibu" : "wanita yang telah melahirkan seseorang",
        "anak" : " orang yang berasal dari atau dilahirkan di (suatu negeri, daerah, dan sebagainya)"
    }
    return worddict

def check_input():
    user_input = ent_keyword.get()
    #if user_input in find_word():
    return user_input

btn_search = tk.Button(
    master= window,
    text="Submit",
    command=find_word()
)

window.mainloop()
