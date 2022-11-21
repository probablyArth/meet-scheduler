from CONSTANTS import *
from tkinter import Frame, Listbox
from tkinter.ttk import Button, Entry, Label
from tkinter import messagebox
from ttkthemes import ThemedTk
from models.Schedule import Schedule
from models.User import User


user_orm = User()
schedule_orm = Schedule()
signed_in_user = None


root = ThemedTk(theme="Breeze")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.title("Meet Scheduler")

home_screen = Frame(root)
signup_screen = Frame(root)
login_screen = Frame(root)
dashboard_screen = Frame(root)

home_screen.grid(sticky="NESW")


screens_array = [home_screen, signup_screen, login_screen, dashboard_screen]


def setScreen(screen: Frame):
    for sc in screens_array:
        sc.grid_forget()
    screen.grid(column=1)


goto_home_button = Button(root, text="Home", command=lambda: setScreen(home_screen))
goto_home_button.grid(column=1, row=1)
goto_signup_button = Button(
    root, text="Sign Up", command=lambda: setScreen(signup_screen)
)
goto_signup_button.grid(column=1, row=2)
goto_login_button = Button(root, text="Login", command=lambda: setScreen(login_screen))
goto_login_button.grid(column=1, row=3)


# HOME SCREEN
Label(home_screen, text="Welcome to Meet Scheduler", font=("bold", 22)).grid(row=0)


def removeButtons():
    goto_home_button.grid_forget()
    goto_signup_button.grid_forget()
    goto_login_button.grid_forget()


def signUp(username: str, password: str):
    global signed_in_user
    try:
        res = user_orm.getByCondition(f'name = "{username}"')
        if len(res) != 0:
            messagebox.showerror(
                title="Already Exists",
                message=f"User with name {username} already exists!",
            )
            return
        user_id = user_orm.insert(username, password)
        schedule_orm.insert(
            user_id,
            "09:00-14:00",
            "09:00-14:00",
            "09:00-14:00",
            "09:00-14:00",
            "09:00-14:00",
            "09:00-14:00",
            "09:00-14:00",
        )
        messagebox.showinfo(title="Success", message="User created successfully!")
        setScreen(dashboard_screen)
        removeButtons()
        signed_in_user = user_id
        updateSchedule()
        populate_listbox()
    except Exception as e:
        print(e)
        messagebox.showerror(
            title="Error", message="An error occured while signing up :("
        )


def logIn(username: str, password: str):
    global signed_in_user
    try:
        res = user_orm.getByCondition(f'name = "{username}"')
        if len(res) == 0:
            messagebox.showerror(
                title="404!", message=f"User with name {username} doesn't exist!"
            )
            return
        if password != res[0][2]:
            messagebox.showerror(title="Forbidden", message=f"Incorrect Password!")
            return
        messagebox.showinfo(title="Success", message="User logged in successfully!")
        setScreen(dashboard_screen)
        signed_in_user = res[0][0]
        updateSchedule()
        removeButtons()
        populate_listbox()
    except Exception as e:
        print(e)
        messagebox.showerror(
            title="Error", message="An error occured while logging in :("
        )


# SIGNUP SCREEN
Label(signup_screen, text="Name").grid(row=0, column=0)
Label(signup_screen, text="Password").grid(row=1, column=0)
signup_username = Entry(signup_screen)
signup_username.grid(row=0, column=1)
signup_password = Entry(signup_screen)
signup_password.grid(row=1, column=1)
signup_button = Button(
    signup_screen,
    text="Sign Up",
    command=lambda: signUp(signup_username.get(), signup_password.get()),
).grid(row=2, column=0)


# LOGIN SCREEN
Label(login_screen, text="Name").grid(row=0, column=0)
Label(login_screen, text="Password").grid(row=1, column=0)
login_username = Entry(login_screen)
login_username.grid(row=0, column=1)
login_password = Entry(login_screen)
login_password.grid(row=1, column=1)
Button(
    login_screen,
    text="Login",
    command=lambda: logIn(login_username.get(), login_password.get()),
).grid(row=2, column=0)

# DASHBOARD SCREEN
Label(dashboard_screen, text="DASHBOARD").grid(row=0, column=0)


dashboard_home_frame = Frame(dashboard_screen)
update_schedule_frame = Frame(dashboard_screen)
book_schedule_frame = Frame(dashboard_screen)
dashboard_frames_array = [
    dashboard_home_frame,
    update_schedule_frame,
    book_schedule_frame,
]

dashboard_home_frame.grid(column=1)


def setDashboardFrame(screen: Frame):
    for sc in dashboard_frames_array:
        sc.grid_forget()
    screen.grid(column=1)


def updateSchedule():
    data = schedule_orm.getByCondition(f"userId = {signed_in_user}")[0]
    monday_label.config(text=data[1])
    tuesday_label.config(text=data[2])
    wednesday_label.config(text=data[3])
    thursday_label.config(text=data[4])
    friday_label.config(text=data[5])
    saturday_label.config(text=data[6])
    sunday_label.config(text=data[7])


monday_label = Label(update_schedule_frame, text="")
monday_label.grid(row=1, column=3)
tuesday_label = Label(update_schedule_frame, text="")
tuesday_label.grid(row=2, column=3)
wednesday_label = Label(update_schedule_frame, text="")
wednesday_label.grid(row=3, column=3)
thursday_label = Label(update_schedule_frame, text="")
thursday_label.grid(row=4, column=3)
friday_label = Label(update_schedule_frame, text="")
friday_label.grid(row=5, column=3)
saturday_label = Label(update_schedule_frame, text="")
saturday_label.grid(row=6, column=3)
sunday_label = Label(update_schedule_frame, text="")
sunday_label.grid(row=7, column=3)


# Dashboard Home Screen
Button(
    dashboard_home_frame,
    text="Update Schedule",
    command=lambda: setDashboardFrame(update_schedule_frame),
).grid()
Button(
    dashboard_home_frame,
    text="Book a Schedule",
    command=lambda: setDashboardFrame(book_schedule_frame),
).grid()

# Update schedule FRAME

Label(update_schedule_frame, text="Update your schedule").grid(row=0, column=1)
Label(update_schedule_frame, text="Monday").grid(row=1, column=0)
Label(update_schedule_frame, text="Tuesday").grid(row=2, column=0)
Label(update_schedule_frame, text="Wednesday").grid(row=3, column=0)
Label(update_schedule_frame, text="Thursday").grid(row=4, column=0)
Label(update_schedule_frame, text="Friday").grid(row=5, column=0)
Label(update_schedule_frame, text="Saturday").grid(row=6, column=0)
Label(update_schedule_frame, text="Sunday").grid(row=7, column=0)

in_monday = Entry(update_schedule_frame)
in_monday.grid(row=1, column=1)
in_tuesday = Entry(update_schedule_frame)
in_tuesday.grid(row=2, column=1)
in_wednesday = Entry(update_schedule_frame)
in_wednesday.grid(row=3, column=1)
in_thursday = Entry(update_schedule_frame)
in_thursday.grid(row=4, column=1)
in_friday = Entry(update_schedule_frame)
in_friday.grid(row=5, column=1)
in_saturday = Entry(update_schedule_frame)
in_saturday.grid(row=6, column=1)
in_sunday = Entry(update_schedule_frame)
in_sunday.grid(row=7, column=1)


def update_schedule():
    schedule_orm.update(
        in_monday.get(),
        in_tuesday.get(),
        in_wednesday.get(),
        in_thursday.get(),
        in_friday.get(),
        in_saturday.get(),
        in_sunday.get(),
    )
    messagebox.showinfo(title="Success", message="Schedule updated successfully!")
    updateSchedule()


Button(update_schedule_frame, text="Update", command=update_schedule).grid()
Button(
    update_schedule_frame,
    text="Go Back",
    command=lambda: setDashboardFrame(dashboard_home_frame),
).grid()

Button(
    book_schedule_frame,
    text="Go Back",
    command=lambda: setDashboardFrame(dashboard_home_frame),
).grid()

list_box_idx = 1


def populate_listbox():
    global list_box_idx
    users = user_orm.getAll()
    for record in users:
        if record[0] != signed_in_user:
            user_list_box.insert(list_box_idx, record[:2])
            list_box_idx += 1


# BOOK SCHEDULE FRAME
def print_selected(event):
    selected_index = user_list_box.curselection()
    data = schedule_orm.getByCondition(
        f"userId = {user_list_box.get(selected_index)[0]}"
    )[0]
    print(data)
    monday_label_booking.config(text=data[1])
    tuesday_label_booking.config(text=data[2])
    wednesday_label_booking.config(text=data[3])
    thursday_label_booking.config(text=data[4])
    friday_label_booking.config(text=data[5])
    saturday_label_booking.config(text=data[6])
    sunday_label_booking.config(text=data[7])


Label(book_schedule_frame, text="Book a schedule").grid()
user_list_box = Listbox(book_schedule_frame)
user_list_box.bind("<<ListboxSelect>>", print_selected)
user_list_box.grid(column=0, rowspan=7)
Label(book_schedule_frame, text="Monday").grid(row=1, column=1)
Label(book_schedule_frame, text="Tuesday").grid(row=2, column=1)
Label(book_schedule_frame, text="Wednesday").grid(row=3, column=1)
Label(book_schedule_frame, text="Thursday").grid(row=4, column=1)
Label(book_schedule_frame, text="Friday").grid(row=5, column=1)
Label(book_schedule_frame, text="Saturday").grid(row=6, column=1)
Label(book_schedule_frame, text="Sunday").grid(row=7, column=1)

monday_label_booking = Label(book_schedule_frame, text="")
monday_label_booking.grid(row=1, column=3)
tuesday_label_booking = Label(book_schedule_frame, text="")
tuesday_label_booking.grid(row=2, column=3)
wednesday_label_booking = Label(book_schedule_frame, text="")
wednesday_label_booking.grid(row=3, column=3)
thursday_label_booking = Label(book_schedule_frame, text="")
thursday_label_booking.grid(row=4, column=3)
friday_label_booking = Label(book_schedule_frame, text="")
friday_label_booking.grid(row=5, column=3)
saturday_label_booking = Label(book_schedule_frame, text="")
saturday_label_booking.grid(row=6, column=3)
sunday_label_booking = Label(book_schedule_frame, text="")
sunday_label_booking.grid(row=7, column=3)

root.mainloop()
