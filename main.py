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
#import db from firebase in order to implement reading
from firebase_admin import db
#configure and initializafirebase
cred = credentials.Certificate("./config/byu-cs111-firebase-adminsdk-ve0lu-d5670a8f24.json")
db = "https://byu-cs111-default-rtdb.firebaseio.com/";
firebase_admin.initialize_app(cred, {'databaseURL': db} )




def login():
        validate = True
        while validate == True:
            user = str(input("Write your email address: "))
            pwd = str(input("Write your password: "))
            loginWithFirebase(user,pwd)

def signUp():
    name = str(input("Write your name please: "))
    user = str(input("Write your email address: "))
    pwd = str(input("Write your password: "))
    signUpWithFirebase(user,name, pwd)

def logOut():
    print("Thanks for using Life Corp App")

def errorInvalidOption():
    print("Sorry, this is an incorrect option...")

def loginWithFirebase(user, pwd):
    print(f"Validando... User: {user}")
    #success, go to homeMenu
    #failure case, return to login

def signUpWithFirebase(user,name, pwd):
    print(f"Creando usuario... {name}")
    #success redirect to login
    #failure case redirect to startMenu

def startMenu():
    begin = True
    while begin == True:
        print("*** Life Corporation App ***")
        print("1. Login")
        print("2. Create a new account")
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


# user is an object with this form
def homeMenu(user):
    print(f"Welcome {user.name}!")
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
    

