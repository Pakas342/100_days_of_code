import json
from tkinter import *
from tkinter import messagebox
from main import create_password
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    new_website = website.get()
    new_email = email.get()
    new_password = password.get()
    new_data = {
        new_website: {
            "email": new_email,
            "password": new_password,
        }
    }

    if len(new_website) == 0 or len(new_email) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Empty data", message="You left some info empty")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                json_data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open(file="passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open(file="passwords.json", mode="w") as file:
                json_data.update(new_data)
                json.dump(json_data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


def random_password():
    password.delete(0, END)
    password_to_add = create_password()
    password.insert(0, password_to_add)
    pyperclip.copy(password_to_add)


def search_website():
    website_to_search = website.get()
    if len(website_to_search) == 0:
        messagebox.showinfo(title="Empty data", message="You left the website empty")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                json_data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showinfo(title="Empty data", message="You don't have any passwords yet")
        else:
            try:
                messagebox.showinfo(title=website_to_search, message=f"Email: {json_data[website_to_search]['email']}\n"
                                                                     f"Password: {json_data[website_to_search]['password']}")
            except KeyError:
                messagebox.showinfo(title="Empty data", message=f"You don't have info for {website_to_search}")

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

website = Entry(width=21)
website.grid(row=1, column=1, sticky="EW")
website.focus()
email = Entry(width=35)
email.grid(row=2, column=1, columnspan=2, sticky="EW")
email.insert(0, "jcbp1999@gmail.com")
password = Entry(width=21)
password.grid(row=3, column=1, sticky="EW")
generate_pass_button = Button(text="Generate Password", command=random_password)
generate_pass_button.grid(row=3, column=2, sticky="EW")
search_website = Button(text="Search Website", command=search_website)
search_website.grid(row=1, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()