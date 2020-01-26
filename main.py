from tkinter import *
from PIL import ImageTk, Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("PROTO Password Credentials Repository").sheet1
sheet2 = client.open("PROTO Journal Submissions Repository").sheet1

data2 = sheet.get_all_records()
data = sheet.get_all_records()

# pprint(data2)

row = sheet.row_values(1)
col = sheet.col_values(1)
col2 = sheet2.col_values(1)
cel = sheet.cell(2, 1).value
col2.pop(0)
# print(col2)
# test = "Feet"
# insertRow = ["{}".format(test)]
# sheet.insert_row(insertRow, 1)

col = [x.strip() for x in col]  # Gets rid of all of the \n and stuff and spaces
col2 = [x.strip() for x in col2]  # Gets rid of all of the \n and stuff and spaces'
col.pop(0)

# pprint(col2)

"""End of thing"""

root = Tk()
root.title("PROTO: Pre-Alpha Release")
root.geometry("1300x700")
root.resizable(0, 0)
my_img1 = ImageTk.PhotoImage(Image.open("etalabx03L.jpg"))
root.configure(bg="#f2f2f2")

background = Label(image=my_img1)
background.pack(side=LEFT)

frame = LabelFrame(root, text="PROTO", padx=5, pady=5, font=("Courier", 45), bg="#e6e6e6")
frame.pack(padx=10, pady=10, side=RIGHT)

usernameEntry = Entry(frame, width=40, bg="#e6e6e6", fg="Black", borderwidth=4)
usernameEntry.grid(row=1, column=1, columnspan=2)
usernameEntry.insert(0, "Enter Your Username:")  # Default text
passwordEntry = Entry(frame, width=40, bg="#e6e6e6", fg="Black", borderwidth=4)
passwordEntry.grid(row=2, column=1, columnspan=2)
passwordEntry.insert(0, "Enter Your Password:")  # Default text


def writeEntree(nameText, dateText, bodyText):
    writeName = nameText.get()
    writeDate = dateText.get()
    writeBody = bodyText.get()
    finishedentree = ["{}\n{}\n{}".format(writeName, writeDate, writeBody)]
    sheet2.insert_row(finishedentree, 2)
    print("Done")

def newentree():
    entrefreme = Toplevel()
    journalframe = LabelFrame(entrefreme, text="New Entree", padx=2, pady=2, font=("Helvetica", 45))
    journalframe.pack(padx=10, pady=10, side=LEFT)
    nameLabel = Label(journalframe, text="Write your name:")
    dateLabel = Label(journalframe, text="Write the date:")
    bodyLabel = Label(journalframe, text="Write your entree:")
    nameText = Entry(journalframe, width=50, borderwidth=4)
    dateText = Entry(journalframe, width=50, borderwidth=4)
    bodyText = Entry(journalframe, width=80, borderwidth=4)
    submit = Button(journalframe, text="Submit", fg="green", font=("Arial", 20), borderwidth=4, command=lambda: writeEntree(nameText, dateText, bodyText))

    nameLabel.grid(row=1, column=1, columnspan=2)
    nameText.grid(row=2, column=1, columnspan=2)
    dateLabel.grid(row=3, column=1, columnspan=2)
    dateText.grid(row=4, column=1, columnspan=2)
    bodyLabel.grid(row=5, column=1, columnspan=2)
    bodyText.grid(row=6, column=1, columnspan=2)
    submit.grid(row=7,column=1,columnspan=2)

    entrefreme.title("New PROTO Entree")


def myClick():  # This gets ran whenever button is pressed
    checkUser = usernameEntry.get()
    checkPass = passwordEntry.get()
    for c in col:
        if c == "{}:{}".format(checkUser, checkPass):
            print("User has logged in")
            efe = Label(frame, text="You have logged in!", bg="#e6e6e6", fg="green")
            efe.grid(row=4, column=1, columnspan=2)
            top = Toplevel()
            lbl = Label(top, text="Attribution: Jason Zhou")

            clientframe = LabelFrame(top, text="Welcome to Proto.", padx=2, pady=2, font=("Helvetica", 45))
            clientframe.pack(padx=10, pady=10)
            test = Button(clientframe, text="New PROTO", width=33, height=20, borderwidth=6, font=("Helvetica", 18),
                          command=newentree)
            test.grid(row=1, column=1)
            test = Button(clientframe, text="My Feed", width=33, height=20, borderwidth=6, font=("Helvetica", 18))
            test.grid(row=1, column=2)

            lbl.pack()
            top.geometry("1000x700")
            top.title("PROTO CLIENT")
        elif c != "{}:{}".format(checkUser, checkPass):
            rwwe = Label(frame, text="Incorrect username or password!", bg="#e6e6e6", fg="red")
            rwwe.grid(row=4, column=1, columnspan=2)


# Client Code


my_label = Label(image=my_img1)
my_label.pack()

yesyes = 0


def goback():
    NoAccount = Button(frame, text="Don't have an account? \n Sign up now for free.", font=("Ariel", 10), bg="#e6e6e6",
                       command=sign_in)  # command is what it does (Refer to function)
    NoAccount.grid(row=3, column=1)
    myButtone = Button(frame, text="Log In", command=myClick, width=12, height=2, font=("Ariel", 10),
                       bg="#e6e6e6")
    myButtone.grid(row=3, column=2)
    return


def register():
    global col
    regUser = usernameEntry.get()
    regPass = passwordEntry.get()
    makeaccount = ["{}:{}".format(regUser, regPass)]
    sheet.insert_row(makeaccount, 2)
    hellore = "Incorrect username or password.".format(usernameEntry.get(), passwordEntry.get())
    re = Label(frame, text="Successfully Registered!", bg="#e6e6e6", fg="green")
    re.grid(row=4, column=1, columnspan=2)
    col = sheet.col_values(1)
    col.pop(0)
    print("Successfully registered.")
    goback()
    print(makeaccount)


def sign_in():
    NoAccount.destroy()
    myButton.destroy()
    NewButt = Button(frame, text="Register", command=register, width=12, height=2, font=("Ariel", 10),
                     bg="#e6e6e6")
    NewButt.grid(row=3, column=2)
    MakeAccount = Button(frame, text="  Have an account?   \n Log in now.", font=("Ariel", 11), bg="#e6e6e6",
                         command=goback)  # command is what it does (Refer to function)
    MakeAccount.grid(row=3, column=1, )
    print("ypo")


NoAccount = Button(frame, text="Don't have an account? \n Sign up now for free.", font=("Ariel", 10), bg="#e6e6e6",
                   command=sign_in)  # command is what it does (Refer to function)
NoAccount.grid(row=3, column=1, )
myButton = Button(frame, text="Log In", command=myClick, width=12, height=2, font=("Ariel", 10),
                  bg="#e6e6e6")  # command is what it does (Refer to function)
myButton.grid(row=3, column=2)  # There needs no inside () for functions using commands ^

# state=DISABLED (right after "text="Touch me!",) will turn the button into a locked buttom


root.mainloop()
