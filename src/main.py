from functools import partial
import tkinter as tk

from game_logic import getLines, getTeam, placeColor, getTeams, checkWin, resetGrid

root = tk.Tk()
root.geometry("1200x600")
root.resizable(width=False, height=False)

color_to_place = "r"
who_to_play = None
number_of_win = {"r": 0, "y":0}

def translateColor(color):
    if color == "r" : return "rouge"
    if color == "y" : return "jaune"

def createCanva():
    return tk.Canvas(root,width=550, height=475, bg="blue")

canva = None

def clear(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()


def stop():
    root.destroy()

def gameOver(color, menu, replay):
    clear(root)
    tk.Label(root, text=f"C'est le joueur {translateColor(color)} qui a gagné!",fg="black",font=("Arial", 30)).place(anchor="center",relx=0.5, rely=0.5)
    tk.Button(root, text="Retourner au menu", fg="black", command= menu).place(anchor="center", relx=0.5, rely= 0.95)
    tk.Button(root, text="Rejouer une partie", fg="black", command=lambda: replay(menu)).place(anchor="center", relx=0.5, rely= 0.85)

def gamePlace(i, menu, replay):
    global color_to_place
    if placeColor(color_to_place, i):
        if checkWin(color_to_place):
            resetGrid()
            gameOver(color_to_place, menu, replay)
            number_of_win[color_to_place] += 1
            color_to_place = "r"
            print(number_of_win)
            return
        for color in getTeams():
            if color != color_to_place:
                color_to_place = color
                break
        for n in range (6):
            for i in range(7):
                if getLines()[n][i] == "y":
                    canva.create_oval(25+75*i,25+75*n,25+50+75*i,25+50+75*n, tags="square"+str(n)+ "," +str(i),fill="yellow")
                elif getLines()[n][i] == "r":
                    canva.create_oval(25+75*i,25+75*n,25+50+75*i,25+50+75*n, tags="square"+str(n)+ "," +str(i),fill="red")
                else:
                    canva.create_oval(25+75*i,25+75*n,25+50+75*i,25+50+75*n, tags="square"+str(n)+ "," +str(i),fill="white")
        who_to_play.configure(text=f"C'est au {translateColor(color_to_place)} de jouer.")
        who_to_play.place(relx = 0.05, rely=0.5)

def menuFromGame(menu):
    global color_to_place
    resetGrid()
    color_to_place = "r"
    menu()

def start(menu):
    clear(root)
    global canva, who_to_play
    canva = createCanva()
    buttons = []
    who_to_play = tk.Label(root, text=f"C'est au {translateColor(color_to_place)} de jouer.",font=("Arial", 16))
    who_to_play.place(relx = 0.05, rely=0.5)
    for i in range(7):
        buttons.append(tk.Button(root, bg="blue", command=partial(gamePlace, i, menu, start)))
        buttons[i].place(relx=0.3125 + (0.0625)*i, rely=0.1, width=60, height=60, anchor="center")
    canva.place(x=1200/2-550/2, y = 600/2-475/2)
    for n in range (6):
        for i in range(7):
            canva.create_oval(25+75*i,25+75*n,25+50+75*i,25+50+75*n, tags="square"+str(n)+ "," +str(i),fill="white")
    tk.Misc.lift(canva)
    for i in range(len(getTeams())):
        tk.Label(root, text=f"Le joueur {translateColor(getTeam(i))} a {number_of_win[getTeam(i)]} victoires.", font=("Arial", 14)).place(anchor='center', rely=0.4+0.2*i, relx=0.85)
    tk.Button(root, text="Retourner au menu", fg="black", command=lambda: menuFromGame(menu)).place(anchor="center", relx=0.5, rely= 0.95)

def main_menu():
    clear(root)
    Label_middle = tk.Label(root, text="Connect-4 game", font=("Arial"), fg="black")
    Button_start = tk.Button(
        root, text="Lancer une partie", fg="black", command=lambda: start(main_menu)
    )
    Button_exit = tk.Button(root, text="Fermer le jeu", fg="black", command=stop)

    Label_middle.pack()
    Button_start.place(relx=0.5, rely=0.45, anchor="center")
    Button_exit.place(relx=0.5, rely=0.55, anchor="center")


main_menu()
root.mainloop()
