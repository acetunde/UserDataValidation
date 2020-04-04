import random
import string
import tkinter
import tkinter.messagebox
import tkinter.simpledialog


class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass

#a dictionary to contain the user data
user = {
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": ""
}

user_list = [] #this list will store the dictionaries created for each user data


def display_output(word): #to display the user's entry
    output = ("Name: %s\nLast Name: %s\nEmail: %s\nPassword: %s" % (user["first_name"], user["last_name"], user["email"], word))
    tkinter.messagebox.showinfo(title="User Information", message=output)


def obtain_input(): #to generate password and add user entry to a list after clicking submit
    user["first_name"] = fname.get()
    user["last_name"] = lname.get()
    user["email"] = emil.get()
    fname.delete(0, tkinter.END)#deletes the entry from the field after clicking "Submit"
    lname.delete(0, tkinter.END)
    emil.delete(0, tkinter.END)
    random_str = ""
    pwd = ""
    try:
        for i in range(5):
            letters = string.ascii_lowercase
            random_str += random.choice(letters)
        pwd = user["first_name"][0] + user["first_name"][1] + user["last_name"][-2] + user["last_name"][-1]
        pwd = pwd + random_str
        message = "Your default password is \"%s\". Do you want to change it?" % pwd
        response = tkinter.messagebox.askquestion(title="Password", message=message,)
        if response == "yes":
            while True:
                try:
                    pwd = tkinter.simpledialog.askstring(title="New Password", prompt="Please enter a new password")
                    if len(pwd) < 7:
                        raise ValueTooSmallError
                    else:
                        break
                except ValueTooSmallError:
                    tkinter.messagebox.showerror(title="Error", message="Password cannot be less than 7 characters")
            display_output(pwd)
        else:
            display_output(pwd)
    except IndexError:
        tkinter.messagebox.showerror(title="Error", message="Fields cannot be empty or less than 2 characters")
    user["password"] = pwd
    m = user["first_name"] + user["last_name"]
    m = user.copy()
    user_list.append(m)

master = tkinter.Tk()
master.geometry("400x200")

master.title("Input Form")

label = tkinter.Label(master, text="Please fill the fields below").grid(row=0)
tkinter.Label(master, text="First Name").grid(row=1)
tkinter.Label(master, text="Last Name").grid(row=2)
tkinter.Label(master, text="E-mail").grid(row=3)

fname = tkinter.Entry(master)
lname = tkinter.Entry(master)
emil = tkinter.Entry(master)

fname.grid(row=1, column=1)
lname.grid(row=2, column=1)
emil.grid(row=3, column=1)

tkinter.Button(master, text="Submit", command=obtain_input).grid(row=5, column=1)
tkinter.Button(master, text="Close", command=master.quit).grid(row=5, column=2)
tkinter.Label(master, text="Click 'Submit' to submit your entry").grid(row=6)
tkinter.Label(master, text="Click 'Close' to exit").grid(row=7)

master.mainloop()

#prints each dictionary in the list
for y in user_list:
    print(f'Name: {y["first_name"]} {y["last_name"]}, Email: {y["email"]}, Password: {y["password"]}')