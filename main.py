import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("PROTO Password Credentials Repository").sheet1

data = sheet.get_all_records()

row = sheet.row_values(1)
col = sheet.col_values(1)
cel = sheet.cell(2,1).value

col = [x.strip() for x in col] # Gets rid of all of the \n and stuff and spaces
col.pop(0)


def isAccount(logUser, logPass, num_lines, islist, search):
    for c in col:
        if c == "{}:{}".format(logUser, logPass):
            print("You have logged in: Method 2")
        islist = num_lines - search
        if col[islist] == "{}:{}".format(logUser, logPass):
            print("You have logged in!")
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


testing1 = 1
testing2 = 2
testing2 = testing2 - testing1
testvariable = 1
testvariable += 1

already = input("Hello and Welcome to Proto! Do you have a an account with us? (y/n): ")
if already.lower().strip() == "n":
    register()
if already.lower().strip() == "y":
    login()
