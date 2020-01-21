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



def mainmenu(logUser, logPass):
    global query
    index = col.index("{}:{}".format(logUser, logPass))
    index += 1
    print("Choices: \"NewEntree\",\"MyFeed\" ")
    e = input("Hello and welcome back to Proto! What would you like to do? ")
    if e.lower().strip() == "newentree":
        name = input("What is your name? ")
        time = input("Please input the date. ")
        print("New journal entree made. Please right your entree.")
        entree = input()
        print("Saving...")
        finishedentree = ["{}\n{}\n{}".format(name, time, entree)]
        sheet2.insert_row(finishedentree, 2)
        print("TIP: To see your entree in MyFeed, restart the client.")
        # makeaccount = ["{}:{}".format(username, password)]
        # sheet.insert_row(makeaccount, 3)
        mainmenu(logUser, logPass)
    elif e.lower().strip() == "myfeed":
        for c in col2:
            print(c)
        mainmenu(logUser, logPass)


def isAccount(logUser, logPass, num_lines, islist, search):
    for c in col:
        if c == "{}:{}".format(logUser, logPass):
            print("You have logged in: Method 2")
        islist = num_lines - search
        if col[islist] == "{}:{}".format(logUser, logPass):
            print("You have logged in!")
            mainmenu(logUser, logPass)
        else:
            search += 1


def login():
    islist = 0
    num_lines = len(col) - 1
    print("Please log in.")
    logUser = input("Username: ")
    logPass = input("Password: ")
    search = 0
    isAccount(logUser, logPass, num_lines, islist, search)


def register():
    global col
    print("Sign up now for free!")
    username = input("Please input a username. ")
    password = input("Please input a password. ")
    confirm = input("Please confirm your password. ")
    if confirm == password:
        makeaccount = ["{}:{}".format(username, password)]
        sheet.insert_row(makeaccount, 2)
        print("Successfully registered.")
        col = sheet.col_values(1)
        col.pop(0)
        login()
    elif confirm != password:
        print("Your passwords do not match up! Please try again.")
        register()

already = input("Hello and Welcome to Proto! Do you have a an account with us? (y/n): ")
if already.lower().strip() == "n":
    register()
if already.lower().strip() == "y":
    login()
