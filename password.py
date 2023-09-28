from tkinter import *
from tkinter import messagebox
from main import create_password
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    new_website = website.get()
    new_email = email.get()
    new_password = password.get()

    if len(new_website) == 0 or len(new_email) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Empty data", message="You left some info empty")
    else:
        is_ok = messagebox.askokcancel(title=new_website, message=f"This are the details that you entered"
                                                                  f"\nEmail: {new_email}"
                                                                  f"\nPassword: {new_password}\nWebsite: {new_website}"
                                                                  f"\nis it ok to save?")
        if is_ok:
            with open(file="passwords.txt", mode="a") as file:
                file.write(f"{new_website} | {new_email} | {new_password}\n")
                website.delete(0, END)
                password.delete(0, END)


def random_password():
    password.delete(0, END)
    password_to_add = create_password()
    password.insert(0, password_to_add)
    pyperclip.copy(password_to_add)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email / Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2, sticky="EW")
website.focus()
email = Entry(width=35)
email.grid(row=2, column=1, columnspan=2, sticky="EW")
email.insert(0, "jcbp1999@gmail.com")
password = Entry(width=21)
password.grid(row=3, column=1, sticky="EW")
generate_pass_button = Button(text="Generate Password", command=random_password)
generate_pass_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()