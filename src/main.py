import tkinter as tk
import os
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry("1200x600")
root.resizable(width=False, height=False)

color_to_place = "red"


def translate(color):
    if color == "red":
        return "rouge"
    if color == "jaune":
        return "jaune"
    else:
        return None


def clear(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()


def stop():
    root.destroy()


def start(menu):
    clear(root)
    # Label_place.place(relx=0.5, rely=0.05, anchor="center")
    image = Image.open(os.getcwd() + "/src/images/Connect4Board.png")
    test = ImageTk.PhotoImage(image=image)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(relx=0.5, rely=0.5, anchor="center")
    # Button_main_menu.place(relx=0.5, rely=0.80, anchor="center")


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
