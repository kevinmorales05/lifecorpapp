# Integrate firebase
"""
path_file of the certificate: obtain in the Firebase console. Authentication // private key in JSON format.
cred_object: 
databaseURL: url de Real Time Database
TO DO: use as a environmental variables.
"""
#import firebase
import firebase_admin
from firebase_admin import credentials
# import db from firebase in order to implement reading
from firebase_admin import db
#configure and initializafirebase
cred = credentials.Certificate(
    "./config/byu-cs111-firebase-adminsdk-ve0lu-d5670a8f24.json")
dbURL = "https://byu-cs111-default-rtdb.firebaseio.com/"
firebase_admin.initialize_app(cred, {'databaseURL': dbURL})
# Reference of the Database Users
refUsers = db.reference("/users")
# Reference of the Database Products
refProducts = db.reference("/products")




def login():
    validate = True
    while validate == True:
        user = str(input("Write your email address: "))
        pwd = str(input("Write your password: "))
        #call login with Firebase
        userLogged = loginWithFirebase(user, pwd)
        #validate userLogged
        if userLogged != None :
            validate = False
            homeMenu(userLogged)
        


def signUp():
    name = str(input("Write your name please: "))
    email = str(input("Write your email address: "))
    pwd = str(input("Write your password: "))
    signUpWithFirebase(email, name, pwd)

def logOut():
    print("Thanks for using Life Corp App")


def errorInvalidOption():
    print("Sorry, this is an incorrect option...")


def loginWithFirebase(user, pwd):
    print(f"Validando... User: {user}")
    # success, go to homeMenu
    # failure case, return to login
    userDatabase = refUsers.get()
    for key, value in userDatabase.items():
        if (value['email'] == user and value['pwd'] == pwd):
            print()
            print("The login was successfull")
            print(f"************************")
            print()
            return value
        else:
            print("Invalid credentials, try again...")
            return None
    #print("This is the obtained email",getEmail)

def signUpWithFirebase(email, name, pwd):
    print(f"Creando usuario... {name}")
    # success redirect to login
    # failure case redirect to startMenu
    user = {
        "name": name,
        "email": email,
        "pwd": pwd
    }
    refUsers.push().set(user)
    print("Account created successfully!")
    


def startMenu():
    begin = True
    while begin == True:
        print("*** Life Corporation App ***")
        print("1. Login")
        print("2. Create a new account")
        print("0. Exit")
        op = input("Choose an option to continue: ")
        if op == '0':
            begin = False
            logOut()
        elif op == '1':
            print("Call login function")
            login()
        elif op == '2':
            print("Call sign up function")
            signUp()
        else:
            errorInvalidOption()


# user is an object with this form
def homeMenu(user):
    print(f"Welcome {user['name']}!")
    begin = True
    while begin == True:
        print("*** Life Corporation App ***")
        print("1. Show products")
        print("2. Create  new product")
        print("3. Delete a product")
        print("4. Analize a product")
        print("0. Exit")
        op = int(input("Choose an option to continue: "))
        if op == 0:
            begin = False
            logOut()
        elif op == 1:
            print("Call login function")
            login()
        elif op == 2:
            print("Call sign up function")
            signUp()
        else:
            errorInvalidOption()


startMenu()
