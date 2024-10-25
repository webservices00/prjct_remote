# Built by VilmaoTech.
import pyautogui as pag
import tkinter as tk
# Creating the opening codes
def max():
    print(f'OPENING: max')
    pag.press("win")
    pag.write("https://play.max.com/home")
    pag.press("enter")

def dineyplus():
    print(f'OPENING: Disney+')
    pag.press("win")
    pag.write("https://disneyplus.com/hu-hu/home")
    pag.press("enter")
    
def netflix():
    print(f'OPENING: Netflix')
    pag.press("win")
    pag.write("https://netflix.com/browse")
    pag.press("enter")
    
def skysho():
    print(f'OPENING: Skyshowtime')
    pag.press("win")
    pag.write("https://skyshowtime.com/watch/home")
    pag.press("enter")
w = tk.Tk()
w.title('PRJCT_REMOTE {0.1.1}')
w.geometry("500x700")
header = tk.Label(w, text="PRJCT_REMOTE  - HOME")
header.pack()

maxbtn = tk.Button(w, text="max", command=max, font=("Times New Roman", 25, "bold"))
maxbtn.pack()

dpbtn = tk.Button(w, text="Disney+", command=dineyplus, font=("Times New Roman", 25, "bold"))
dpbtn.pack()

netflixbtn = tk.Button(w, text="Netflix", command=netflix, font=("Times New Roman", 25, "bold"))
netflixbtn.pack()

skyshobtn = tk.Button(w, text="SkyShotime", command=skysho, font=("Times New Roman", 25, "bold"))
skyshobtn.pack()





footer = tk.Label(w, text="© 2024 VilmaoTech")
footer.pack()
w.mainloop()