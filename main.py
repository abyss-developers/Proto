

def isAccount(logUser, logPass, num_lines, islist, search):
  for c in credentials:
    if c == "{}:{}".format(logUser, logPass):
      print("You have logged in: Method 2")
    islist = num_lines - search 
    if credentials[islist] == "{}:{}".format(logUser, logPass):
      print("You have logged in!")
    else:
      search += 1
      
def login():
  islist = 0
  num_lines = len(credentials) - 1
  print("Please log in.")
  logUser = input("Username: ")
  logPass = input("Password: ")
  search = 0
  isAccount(logUser, logPass, num_lines, islist, search)

def register():
  print("Sign up now for free!")
  username = input("Please input a username. ")
  password = input("Please input a password. ")
  confirm = input("Please confirm your password. ")
  if confirm == password:
    f = open("credentials.txt", "a")
    f.write("\n{}:{}".format(username,password))
    f.close()
    print("Successfully registered.")
    login()
  elif confirm != password:
    print("Your passwords do not match up! Please try again.")
    register()

testing1 = 1
testing2 = 2
testing2 = testing2 - testing1
testvariable = 1
testvariable += 1

f = open("credentials.txt", "r")
credentials = f.readlines()
credentials = [x.strip() for x in credentials]
credentials.pop(0)

already = input("Hello and Welcome to Proto! Do you have a an account with us? (y/n): ")
if already.lower().strip() == "n":
  register()
if already.lower().strip() == "y":
  login()
