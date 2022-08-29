import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ------------------------- SEARCH FOR WEBSITE ----------------------------- #
def search():
    website = website_entry.get().lower()
    if website_entry.get() != '':
        try:
            with open("data.json", "r") as data_file:
                passwords = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error!", message="You don't have any saved passwords!")
        else:
            if website in passwords:
                email = passwords[website]['email']
                password = passwords[website]['password']
                print(email)
                messagebox.showinfo(title=website, message=f"Email/Username: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error!", message="A email/username or password have not been associated with that website")
    else:
        messagebox.showerror(title="Error!", message="You did not give a valid website.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().lower()
    print(website)
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email)==0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                passwords = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=1)

        else:
            passwords.update(new_data)

        finally:
            if email != MY_EMAIL:
                email_entry.delete(0,END)
                email_entry.insert(0, MY_EMAIL)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

MY_EMAIL= ""

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky= 'ew')
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky= 'ew')
email_entry.insert(0, MY_EMAIL)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky= 'ew')

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
find_button = Button(text="Search", command=search)
find_button.grid(row=1, column= 2, sticky= 'ew')

window.mainloop()