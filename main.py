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
# import python module for regular expressions
import re
#configure and initializafirebase
cred = credentials.Certificate(
    "./config/byu-cs111-firebase-adminsdk-ve0lu-d5670a8f24.json")
dbURL = "https://byu-cs111-default-rtdb.firebaseio.com/"
firebase_admin.initialize_app(cred, {'databaseURL': dbURL})
# Reference of the Database Users
refUsers = db.reference("/users")
# Reference of the Database Products
refProducts = db.reference("/products")

# functions for authentication


def login():
    validate = True
    while validate == True:
        user = str(input("Write your email address: "))
        pwd = str(input("Write your password: "))
        # call login with Firebase
        userLogged = loginWithFirebase(user, pwd)
        # validate userLogged
        if userLogged != 'No':
            validate = False
            homeMenu(userLogged)


def signUp():
    pwd = ""
    print()
    print("Create a new account")
    print(f"************************")
    name = str(input("Write your name please: "))
    email = str(input("Write your email address: "))
    if isValid(email) == True:
        pwd = str(input("Write your password: "))
    else:
        print("The format of the email is incorrect, try again!")
        signUp()
    signUpWithFirebase(name, email, pwd)


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
    print("Invalid credentials, try again...")
    return 'No'


def signUpWithFirebase(name, email, pwd):
    print(f"Creando usuario... {name}")
    # success redirect to login
    # failure case redirect to startMenu
    user = {
        "name": name,
        "email": email,
        "pwd": pwd
    }
    refUsers.push().set(user)
    print()
    print("Account created successfully!")
    print("*****************************")
    print()

# Products Functions

#show products with logic
def showProducts():
    print()
    print("Available Products")
    print(f"************************")
    print()
    getProductsWithFirebase()
#Create product with logic
def createProduct():
    print()
    print("Create a new Product")
    print(f"************************")
    name = str(input("Write the name of the product please: "))
    description = str(input("Describe the product: "))
    target = ""
    fixedCosts = []
    variableCosts = []

    targetStatus = True
    while targetStatus == True:
        print("1. Adults ")
        print("2. Young ")
        print("3. Children ")
        print("4. Every body")
        targetOp = str(input("Choose the target: "))
        if targetOp == "1":
            target = "Adults"
            targetStatus = False
        elif targetOp == "2":
            target == "Young"
            targetStatus = False
        elif targetOp == "3":
            target == "Childern"
            targetStatus = False
        elif targetOp == "4":
            target == "All"
            targetStatus = False
        else:
            errorInvalidOption()
    # getting fixed costs
    fixedStatus = True
    i = 0
    while fixedStatus == True:
        costName = str(input(f"Write the name of the fix cost # {i + 1}: "))
        costDescription = str(input("Describe the fix cost: "))
        cost = str(input("How much is it?: "))
        quantity = str(input("How many units do you need?: "))
        fixedCosts.append(
            {
                "costName": costName,
                "costDescription": costDescription,
                "cost": cost,
                "quantity": quantity
            }
        )
        continueStatus = True
        while continueStatus == True:
            print("1. Yes ")
            print("2. No (continue with variable costs")
            answer = str(input("Do you want to continue adding fixed costs? "))
            if answer == '1':
                continueStatus = False
            elif answer == '2':
                continueStatus = False
                fixedStatus = False
            else:
                errorInvalidOption()
        i = i + 1
    #Minimum persons for the product
    minimunPersons = int(input("How many persons are the minumun to offer the service "))
    ######TO DO handle exception
    #getting variable costs
    variableStatus = True
    j = 0
    while variableStatus == True:
        costName = str(input(f"Write the name of the variable cost # {j}: "))
        costDescription = str(input("Describe the variable cost: "))
        cost = str(input("How much is it?: "))
        quantity = str(input("How many units do you need?: "))
        variableCosts.append(
            {
                "costName": costName,
                "costDescription": costDescription,
                "cost": cost,
                "quantity": quantity
            }
        )
        continueStatus = True
        while continueStatus == True:
            print("1. Yes ")
            print("2. No (finish creating product")
            answer = str(input("Do you want to continue adding variable costs? "))
            if answer == '1':
                continueStatus = False
            elif answer == '2':
                continueStatus = False
                variableStatus = False
            else:
                errorInvalidOption()

        j = j + 1       

    # call function for getting the totalCost per person

    newProduct = {
        "name": name,
        "description": description,
        "target": target,
        "fixedCosts": fixedCosts,
        "variableCosts": variableCosts,
        "totalCostPerPerson": getTotalCostPerPerson(minimunPersons, fixedCosts, variableCosts),
        "minimunPersons": minimunPersons,
        
    }
    createProductWithFirebase(newProduct)
#Delete product with logic
def deleteProduct():
    products = getProductsWithFirebase()
    productsDatabase = refProducts.get()
    op = str(input("Choose the number to delete a product:"))
    #TO DO: handle error
    print("Deleting product")
    for key, val in productsDatabase.items():
        if val['name'] == products[int(op)-1]['name']:
            refProducts.child(key).set({})
    print()        
    print("The product was deleted sucessfully!")
    print('**************************************')
    print()

#analize determined customers  
def analizeProduct():
    print("Product Analysis")
    productsDatabase = getProductsWithFirebase()
    option = str(input("Choose the product: "))
    print("What operation do you want to do")
    print("1. Get the minimum customers to get a determined profit.")
    op = str(input("Choose the option: "))
    profit = str(input("Write the desired profit (USD): "))
    if op == '1':
        print()
        print("This is the analysis")
        print(productsDatabase[int(option)-1]['totalCostPerPerson'])
        print(f"This is the minimum customers: {(float(profit)/float(productsDatabase[int(option)-1]['totalCostPerPerson'])):.2f} in order to get {profit} USD") 
    else:
        errorInvalidOption()
        analizeProduct()
    
# Product analysis functions
# ---- Get total cost Per Person
def getTotalCostPerPerson(numberOfPersons, fixedCosts, variableCosts):
    total = 0
    #sum fixedCosts
    for costUnit in fixedCosts:
        total = total +  float(costUnit['cost']) * numberOfPersons
    # sum variableCosts
    for costUnit in variableCosts:
        total = total +  float(costUnit['cost']) * numberOfPersons   
    return total/numberOfPersons

# Products services
def createProductWithFirebase(newProduct):
    print(f"Creating new product... {newProduct['name']}")
    # success redirect to login
    # failure case redirect to startMenu
    refProducts.push().set(newProduct)
    print()
    print("Product created successfully!")
    print("*****************************")
    print()

def getProductsWithFirebase():
    print(f"Getting... Products")
    # consult products database
    productsDatabase = refProducts.get()
    #return an array
    productsArray = []
    i=0
    for key, value in productsDatabase.items():
        print("****************************")
        print(f"{i + 1}. {value['name']}")
        print(f"Description")
        print(f"{value['description']}")
        print(f"Target: {value['target']}")
        print(f"Total cost per person: {value['totalCostPerPerson']}")
        print(f"Minimum Persons: {value['minimunPersons']}")
        i = i + 1
        productsArray.append(value)
    return productsArray   
 #function to validate email   
def isValid(email):
    emailRegularExpression = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(emailRegularExpression, email) is not None

#First menu, includes login
def startMenu():
    print()
    print("*** Life Corporation App ***")
    print(f"************************")
    print()
    begin = True
    while begin == True:
        print("*** Sign in ***")
        print("1. Login")
        print("2. Create a new account")
        print("0. Exit")
        op = input("Choose an option to continue: ")
        if op == '0':
            begin = False
            logOut()
        elif op == '1':
            login()
        elif op == '2':
            signUp()
        else:
            errorInvalidOption()


#logged menu
def homeMenu(user):
    print()
    print(f"Welcome {user['name']}!")
    print(f"************************")
    print()
    begin = True
    while begin == True:
        print()
        print("*** Life Corporation App ***")
        print(f"************************")
        print()
        print("1. Show products")
        print("2. Create  new product")
        print("3. Delete a product")
        print("4. Analize a product")
        print("0. Exit")
        op = input("Choose an option to continue: ")
        if op == '0':
            begin = False
            logOut()
        elif op == '1':
            showProducts()
        elif op == '2':
            createProduct()
        elif op == '3':
            deleteProduct()
        elif op == '4':
            analizeProduct()
        else:
            errorInvalidOption()
#In order to run test without calling main function
if __name__ == "__main__":
    startMenu()

