# Built by VilmaoTech.
import pyautogui as pag
import tkinter as tk
import time as time

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
    
def search(trueValue: str):
    pag.press("win")
    pag.write(f'{trueValue}')
    pag.press("enter")

def yt():
    pag.press("win")
    pag.write('cmd')
    pag.press("enter")
    time.sleep(3)
    pag.write('chrome --new-window "http://youtube.com/"')
    pag.press("enter")
w = tk.Tk()

w.title('PC Remote')

w.geometry("500x700")

header = tk.Label(w, text="PRJCT_REMOTE  - HOME")
header.pack()

maxbtn = tk.Button(w, text="max", command=max, font=("Times New Roman", 25, "bold"))
maxbtn.pack()

dpbtn = tk.Button(w, text="Disney+", command=dineyplus, font=("Times New Roman", 25, "bold"))
dpbtn.pack()

skyshobtn = tk.Button(w, text="SkyShotime", command=skysho, font=("Times New Roman", 25, "bold"))
skyshobtn.pack()

netflixbtn = tk.Button(w, text="Netflix", command=netflix, font=("Times New Roman", 25, "bold"))
netflixbtn.pack()

ytbtn = tk.Button(w, text="Youtube", command=yt, font=("Times New Roman", 25, "bold"))
ytbtn.pack()


searchlabel = tk.Label(w, text="Search what you need::", font=("Airal", 20, "bold"))
searchlabel.pack()

searchentry = tk.Entry(w, width=32)
searchentry.pack()

def getValueandSearch():
    searchValue: str = searchentry.get()
    print(f'Search:: {searchValue}')
    search(searchValue)
    
    
searchgetbutton = tk.Button(w, text="KERESS!", command=getValueandSearch)
searchgetbutton.pack()


footer = tk.Label(w, text="© 2024 VilmaoTech")
footer.pack()
w.mainloop()