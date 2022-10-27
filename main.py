from turtle import title
from dotenv import load_dotenv
from CONSTANTS import *
from screens import signup

load_dotenv()

from tkinter import Tk, Button


main_screen = Tk()

main_screen.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
main_screen.resizable = False

main_screen.title("Meet Scheduler")

loginButton = Button(main_screen, text="Login")
signUpButton = Button(main_screen, text="Sign Up")

loginButton.pack()
signUpButton.pack()

main_screen.mainloop()
