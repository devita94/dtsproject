import tkinter as tk
from tkinter.constants import X

window = tk.Tk()
window.title("KBBI Apps")

#untuk window
frm_title = tk.Frame(master=window, bg="#317FE2")
frm_title.pack(fill=tk.X, side=tk.LEFT)
label_keyword = tk.Label(text="Cari Kata")
frm_entry = tk.Entry()
btn_search = tk.Button()


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
