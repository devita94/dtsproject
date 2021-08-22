import tkinter as tk
from tkinter.constants import TRUE, X
from typing import Text

window = tk.Tk()
window.title("KBBI Apps")

#untuk window
frame = tk.Frame(master=window, bg="white")
frame.pack(fill=tk.BOTH, expand=TRUE)
title_frame = tk.Label(master = frame, text="Selamat Datang di KBBI Apps", bg="#317FE2")
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
