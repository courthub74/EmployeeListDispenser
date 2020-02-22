from tkinter import *
from tkinter import ttk
import requests
import json

# API retrieve
employees = requests.get("http://api.open-notify.org/astros.json")

# Check for connectivity
print(employees.status_code)
# (connection successful 12/16/2016) <200>

# Extracting the TEXT from the API
data = employees.text
parsed = json.loads(data) # Parsing the text with json loads as string
# print(data)

# extracting the NAMES
# this is how you do it when its a STRING
name1 = parsed["people"][0]["name"]
name2 = parsed["people"][1]["name"]
name3 = parsed["people"][2]["name"]
name4 = parsed["people"][3]["name"]
name5 = parsed["people"][4]["name"]
name6 = parsed["people"][5]["name"]


# Employee FUNCTIONS
# create a variable for each parsed name variable
def employee1():
    namefield1.delete(0.0, 'end')
    first = name1
    namefield1.insert(INSERT, first)


def employee2():
    namefield2.delete(0.0, 'end')
    second = name2
    namefield2.insert(INSERT, second)


def employee3():
    namefield3.delete(0.0, 'end')
    third = name3
    namefield3.insert(INSERT, third)


def employee4():
    namefield4.delete(0.0, 'end')
    fourth = name4
    namefield4.insert(INSERT, fourth)


def employee5():
    namefield5.delete(0.0, 'end')
    fifth = name5
    namefield5.insert(INSERT, fifth)


def employee6():
    namefield6.delete(0.0, 'end')
    sixth = name6
    namefield6.insert(INSERT, sixth)


# LOADS for a string
# parsed = json.loads(data)

app = Tk()
app.title("Personnel List")
app.geometry("500x500")
app.configure(background="Grey")
app.iconbitmap('icons/Personnel.ico')

# Header
Label(app, text="API Employee List Disperser").grid(row=0, column=1, pady=10, padx=20)

# TextField 1
Label(app, text="Personnel 1:").grid(row=1, column=0, pady=10, padx=20)
namefield1 = Text(app, height=1, width=20)
namefield1.grid(row=1, column=1, pady=10, padx=20)

# TextField 2
Label(app, text="Personnel 2:").grid(row=2, column=0, pady=10, padx=20)
namefield2 = Text(app, height=1, width=20)
namefield2.grid(row=2, column=1, pady=10, padx=20)

Label(app, text="Personnel 3:").grid(row=3, column=0, pady=10, padx=20)
namefield3 = Text(app, height=1, width=20)
namefield3.grid(row=3, column=1, pady=10, padx=20)

Label(app, text="Personnel 4:").grid(row=4, column=0, pady=10, padx=20)
namefield4 = Text(app, height=1, width=20)
namefield4.grid(row=4, column=1, pady=10, padx=20)

Label(app, text="Personnel 5:").grid(row=5, column=0, pady=10, padx=20)
namefield5 = Text(app, height=1, width=20)
namefield5.grid(row=5, column=1, pady=10, padx=20)

Label(app, text="Personnel 6:").grid(row=6, column=0, pady=10, padx=20)
namefield6 = Text(app, height=1, width=20)
namefield6.grid(row=6, column=1, pady=10, padx=20)

# SUBMIT BUTTON
Button(app, text="Populate", height=1, width=10,
       command=lambda: [employee1(), employee2(), employee3(),
                        employee4(), employee5(), employee6()]).grid(row=7, column=1, pady=10, padx=20)

app.mainloop()
