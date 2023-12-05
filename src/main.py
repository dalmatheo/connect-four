# The imports
from functools import partial
import tkinter as tk

from game_logic import (
    getLines,
    getTeam,
    placeColor,
    getTeams,
    checkWin,
    resetGrid,
    setTeam,
)


# Initialize constants
CHECKER_SIZE = 25
connect_four_color = "blue"

# Initialize the window
root = tk.Tk()
root.geometry("1200x600")
root.resizable(width=False, height=False)
root.title("Connect-4 game")

# Initialize variables
color_to_place = getTeams()[0]
who_to_play = None
number_of_win = {}
resume_or_start_game = "Lancer une partie"


def teamWins():
    global color_to_place
    for team in getTeams():
        number_of_win.setdefault(team, 0)
    color_to_place = getTeams()[0]


teamWins()


# Function to close the window -> might be removed later
def stop():
    root.destroy()


# Function to translate a color -> might be removed later
def translateColor(color):
    if color == "red":
        return "rouge"
    if color == "yellow":
        return "jaune"
    if color == "blue":
        return "bleu"
    if color == "purple":
        return "violet"
    if color == "orange":
        return "orange"
    if color == "green":
        return "vert"
    if color == "black":
        return "noir"
    if color == "gray":
        return "gris"
    if color == "pink":
        return "rose"


# Function to create a canva -> might be removed later
def createCanva():
    return tk.Canvas(root, width=550, height=475, bg=connect_four_color)


# Function to clear a window
def clear(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()


# Function of game over
def gameOver(color, menu, replay):
    clear(root)
    tk.Label(
        root,
        text=f"C'est le joueur {translateColor(color)} qui a gagné!",
        fg="black",
        font=("Arial", 30),
    ).place(anchor="center", relx=0.5, rely=0.5)
    tk.Button(
        root, text="Retourner au menu", fg="black", font=("Arial"), command=menu
    ).place(anchor="center", relx=0.5, rely=0.95)
    tk.Button(
        root,
        text="Rejouer une partie",
        fg="black",
        font=("Arial"),
        command=lambda: replay(menu),
    ).place(anchor="center", relx=0.5, rely=0.85)


# Function to update the checkers that are shown
def updateGame():
    for n in range(6):
        for i in range(7):
            if getLines()[n][i] == getTeams()[1] or getLines()[n][i] == getTeams()[0]:
                canva.create_oval(
                    CHECKER_SIZE + CHECKER_SIZE * 3 * i,
                    CHECKER_SIZE + CHECKER_SIZE * 3 * n,
                    CHECKER_SIZE + CHECKER_SIZE * 2 + CHECKER_SIZE * 3 * i,
                    CHECKER_SIZE + CHECKER_SIZE * 2 + CHECKER_SIZE * 3 * n,
                    tags="square" + str(n) + "," + str(i),
                    fill=getLines()[n][i],
                )
            else:
                canva.create_oval(
                    CHECKER_SIZE + CHECKER_SIZE * 3 * i,
                    CHECKER_SIZE + CHECKER_SIZE * 3 * n,
                    CHECKER_SIZE + CHECKER_SIZE * 2 + CHECKER_SIZE * 3 * i,
                    CHECKER_SIZE + CHECKER_SIZE * 2 + CHECKER_SIZE * 3 * n,
                    tags="square" + str(n) + "," + str(i),
                    fill="white",
                )
    who_to_play.configure(text=f"C'est au {translateColor(color_to_place)} de jouer.")
    who_to_play.place(relx=0.05, rely=0.5)


# Function to place a checker
def gamePlace(i, menu, replay):
    global color_to_place
    if placeColor(color_to_place, i):
        if checkWin(color_to_place):
            resetGrid()
            gameOver(color_to_place, menu, replay)
            number_of_win[color_to_place] += 1
            color_to_place = getTeams()[0]
            return
        for color in getTeams():
            if color != color_to_place:
                color_to_place = color
                break
        updateGame()


# Function to leave a game
def leaveGame(menu, bool):
    global resume_or_start_game
    if bool:
        global color_to_place
        resetGrid()
        color_to_place = getTeams()[0]
        resume_or_start_game = "Lancer une partie"
        menu()
    else:
        resume_or_start_game = "Reprendre votre partie"
        menu()


# Function to open the menu from a game
def menuFromGame(menu):
    clear(root)
    Label_middle = tk.Label(
        root,
        text="Voulez vous éffacer votre partie en cours?",
        font=("Arial", 16),
        fg="black",
    )
    Button_yes = tk.Button(
        root,
        text="Oui",
        fg="black",
        font=("Arial"),
        command=lambda: leaveGame(menu, True),
    )
    Button_no = tk.Button(
        root,
        text="Non",
        fg="black",
        font=("Arial"),
        command=lambda: leaveGame(menu, False),
    )

    Label_middle.place(anchor="center", relx=0.5, rely=0.4)
    Button_yes.place(relx=0.45, rely=0.5, anchor="center")
    Button_no.place(relx=0.55, rely=0.5, anchor="center")


# Function that starts a game
def start(menu):
    clear(root)
    global canva, who_to_play
    who_to_play = tk.Label(
        root,
        text=f"C'est au {translateColor(color_to_place)} de jouer.",
        font=("Arial", 16),
    )
    canva = createCanva()
    buttons = []
    for i in range(7):
        buttons.append(
            tk.Button(
                root, bg=connect_four_color, command=partial(gamePlace, i, menu, start)
            )
        )
        buttons[i].place(
            relx=0.3125 + (0.0625) * i, rely=0.1, width=60, height=60, anchor="center"
        )
    canva.place(x=1200 / 2 - 550 / 2, y=600 / 2 - 475 / 2)
    updateGame()
    tk.Misc.lift(canva)
    for i in range(len(getTeams())):
        if number_of_win[getTeam(i)] == 1:
            tk.Label(
                root,
                text=f"Le joueur {translateColor(getTeam(i))} a {number_of_win[getTeam(i)]} victoire.",
                font=("Arial", 14),
            ).place(anchor="center", rely=0.4 + 0.2 * i, relx=0.85)
        else:
            tk.Label(
                root,
                text=f"Le joueur {translateColor(getTeam(i))} a {number_of_win[getTeam(i)]} victoires.",
                font=("Arial", 14),
            ).place(anchor="center", rely=0.4 + 0.2 * i, relx=0.85)
    tk.Button(
        root,
        text="Retourner au menu",
        fg="black",
        font=("Arial"),
        command=lambda: menuFromGame(menu),
    ).place(anchor="center", relx=0.5, rely=0.95)


# Function to set the board color.
def setColor(couleur, label):
    global connect_four_color
    colors = [
        "blue",
        "purple",
        "orange",
        "green",
        "black",
        "gray",
        "pink",
        "yellow",
        "red",
    ]
    flag = False
    for color in colors:
        if translateColor(color) == couleur:
            connect_four_color = color
            label.configure(text=f"La couleur {couleur} est valide.")
            return
    label.configure(text=f"La couleur {couleur} n'est pas valide.")


# Function to set the checkers color.
def setColorChecker(team, couleur, label):
    global connect_four_color
    colors = [
        "blue",
        "purple",
        "orange",
        "green",
        "black",
        "gray",
        "pink",
        "yellow",
        "red",
    ]
    flag = False
    if team == 1:
        for color in colors:
            if translateColor(color) == couleur:
                setTeam(0, color)
                teamWins()
                label.configure(text=f"La couleur {couleur} est valide.")
                return
    else:
        for color in colors:
            if translateColor(color) == couleur:
                setTeam(1, color)
                teamWins()
                label.configure(text=f"La couleur {couleur} est valide.")
                return
        label.configure(text=f"La couleur {couleur} n'est pas valide.")


# Function to open the menu to set the checkers color.
def checkerColorSettings(menu):
    clear(root)
    resetGrid()
    Label_error = tk.Label(
        root,
        text="Entrez une couleur valide pour l'un des pions",
        font=("Arial", 18),
        fg="black",
    )
    Label_error.place(anchor="center", relx=0.5, rely=0.4)
    e1 = tk.Entry(root)
    e1.place(anchor="center", relx=0.5, rely=0.45)
    Button_apply_settings_checker1 = tk.Button(
        root,
        text="Appliquer la couleur du pion 1",
        font=("Arial", 14),
        fg="black",
        command=lambda: setColorChecker(1, e1.get(), Label_error),
    )
    Button_apply_settings_checker1.place(anchor="center", relx=0.35, rely=0.55)
    Button_apply_settings_checker1 = tk.Button(
        root,
        text="Appliquer la couleur du pion 2",
        font=("Arial", 14),
        fg="black",
        command=lambda: setColorChecker(2, e1.get(), Label_error),
    )
    Button_apply_settings_checker1.place(anchor="center", relx=0.65, rely=0.55)
    tk.Button(
        root, text="Retourner au menu", fg="black", font=("Arial"), command=menu
    ).place(anchor="center", relx=0.5, rely=0.95)


# Warning that explains that the current game will be deleted
def checkerColorSettingsWarning(menu):
    clear(root)
    Label_middle = tk.Label(
        root,
        text="Cette action effacera votre partie actuelle si vous en avez une. \nVoulez vous procéder ?",
        font=("Arial", 16),
        fg="black",
    )
    Button_yes = tk.Button(
        root,
        text="Oui",
        fg="black",
        font=("Arial"),
        command=lambda: checkerColorSettings(menu),
    )
    Button_no = tk.Button(root, text="Non", fg="black", font=("Arial"), command=menu)

    Label_middle.place(anchor="center", relx=0.5, rely=0.4)
    Button_yes.place(relx=0.45, rely=0.5, anchor="center")
    Button_no.place(relx=0.55, rely=0.5, anchor="center")


# Function to open the menu to set the checkers color.
def boardColorSettings(menu):
    clear(root)
    Label_error = tk.Label(
        root,
        text="Entrez une couleur valide pour le puissance 4",
        font=("Arial", 18),
        fg="black",
    )
    Label_error.place(anchor="center", relx=0.5, rely=0.4)
    Label_middle = tk.Label(root, text="Paramètre", font=("Arial", 18), fg="black")
    Label_middle.place(anchor="center", relx=0.50, rely=0.075)
    e1 = tk.Entry(root)
    e1.place(anchor="center", relx=0.5, rely=0.45)
    Button_apply_settings = tk.Button(
        root,
        text="Appliquer la couleur du puissance 4",
        font=("Arial", 14),
        fg="black",
        command=lambda: setColor(e1.get(), Label_error),
    )
    Button_apply_settings.place(anchor="center", relx=0.5, rely=0.55)
    tk.Button(
        root, text="Retourner au menu", fg="black", font=("Arial"), command=menu
    ).place(anchor="center", relx=0.5, rely=0.95)


# Function to open the menu to go to the settings.
def settingsMenu(menu):
    clear(root)
    Label_menu = tk.Label(
        root, text="Veuillez selectionner un paramètre.", font=("Arial", 18)
    )
    Label_menu.place(anchor="center", relx=0.5, rely=0.45)
    Button_board_color = tk.Button(
        root,
        text="Couleur du puissance 4",
        font=("Arial"),
        command=lambda: boardColorSettings(menu),
    )
    Button_board_color.place(anchor="center", relx=0.42, rely=0.5)
    Button_checkers_color = tk.Button(
        root,
        text="Couleur des pions",
        font=("Arial"),
        command=lambda: checkerColorSettingsWarning(menu),
    )
    Button_checkers_color.place(anchor="center", relx=0.57, rely=0.5)
    tk.Button(
        root, text="Retourner au menu", fg="black", font=("Arial"), command=menu
    ).place(anchor="center", relx=0.5, rely=0.95)


# Function that creates the main menu
def main_menu():
    clear(root)
    Label_middle = tk.Label(root, text="Connect-4 game", font=("Arial"), fg="black")
    Button_start = tk.Button(
        root,
        text=resume_or_start_game,
        fg="black",
        font=("Arial"),
        command=lambda: start(main_menu),
    )
    Button_settings = tk.Button(
        root,
        text="Paramètres",
        fg="black",
        font=("Arial"),
        command=lambda: settingsMenu(main_menu),
    )
    Button_exit = tk.Button(
        root, text="Fermer le jeu", fg="black", font=("Arial"), command=stop
    )

    Label_middle.pack()
    Button_start.place(relx=0.5, rely=0.40, anchor="center")
    Button_settings.place(relx=0.5, rely=0.50, anchor="center")
    Button_exit.place(relx=0.5, rely=0.60, anchor="center")


# Running the game
main_menu()
root.mainloop()
