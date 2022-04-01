def menu():

    print("\n_______________Auto Sales________________")
    print(" ")
    print("[1] view available cars")
    print("[2] View customers ")
    print("[3] Place an Order")
    print("[4] Delete an order")
    print("[5] Create new customer")
    print("[6] Delete a customer")
    print("[7] Update Horse Power")       
    print("[8] read a csv file")  
    print("[9] view csv files")  
    print("[0] Exit") 



# view cars
import datetime
from tabulate import tabulate
from pymongo import MongoClient

def cars_view():    
    try:
        client = MongoClient()
        db = client['tyrone_auto_sales']
        cars = db['cars']
        results = cars.find({},{"_id":0})
        for result in results:
            print(result)

    except Exception as e:
        print(e)        


# print("Add a car")
from pymongo import MongoClient
client = MongoClient()
db = client['tyrone_auto_sales']
cars = db['cars']

def insert():    
    try:
        car = int(input ("orderId:"))
        make = input("Enter Car Make:")
        model = input("Enter Car Model:")
        year = int(input("Enter year:"))
        engine_HP = int(input("Enter HP:"))
        msrp = int(input("Enter MSRP:"))
    
        db.cars.insert_one({
        "_id": car,
        "Make": make,
        "Model":model,  
        "Year": year,
        "Engine HP": engine_HP,
        "MSRP": msrp,
        "Date Added": datetime.datetime.now()         
        })
        print ('\nInserted successfully\n')

    except Exception as e:
        print(e)

# delete a car
from pymongo import MongoClient
client = MongoClient()
db = client['tyrone_auto_sales']
cars = db['cars']

def delete():    
    try:
        make = input("What is the Car Make:")       
    
        db.cars.delete_one({       
        "Make": make
         })
        print ('\nDeleted successfully\n')
    except Exception as e:
        print(e)
        delete()


# delete a customer
from pymongo import MongoClient
client = MongoClient()
db = client['tyrone_auto_sales']
cars = db['customers']

def del_cust(): 

    try:        
        last_Name = input("What is the last name:")   
    
        db.customers.delete_one({       
        "Last Name":last_Name
        })        
        print ('\nDeleted successfully\n')        
    except Exception as e:
        print(e)
        

#update horse power
from pymongo import MongoClient
client = MongoClient()
db = client['tyrone_auto_sales']
cars = db['cars']

def update():    
    try:
        make = input("What is the make of the car:")   
        engine_HP = int(input("What is the hp amount to update:"))    
    
        db.cars.update_one({'Make' :make},{"$set": {"Engine HP":engine_HP}})

        print ('\nUpdated successfully\n')

    except Exception as e:
        print(e)

# Create a new Customer
from pymongo import MongoClient
client = MongoClient()
db = client['tyrone_auto_sales']
customers = db['customers']

def customers():    
    try:
        _id = int(input ("CustomerId:"))
        first_Name = input("Enter First Name:")
        last_Name = input("Enter Last Name:")
        dob = input("Enter Date of Birth:")
           
        db.customers.insert_one({
        "_id": _id,
        "First Name": first_Name,
        "Last Name":last_Name,  
        "Date of Birth": dob,
        "Date Added": datetime.datetime.now()         
        })
       
        print ('\ncustomer info entered successfully\n')

    except Exception as e:
        print(e)
        customers()

# view customers
from bson.objectid import ObjectId
from pymongo import MongoClient
import datetime

def view_customers():    
    try:
        client = MongoClient()
        db = client['tyrone_auto_sales']
        customers= db['customers']
        results = customers.find({},{"_id":0})
        for result in results:
            # print(" ")
            print(result)
    except Exception as e:
        print(e)  

# Read a file
from pymongo import MongoClient
client = MongoClient()
db = client['tyrone_auto_sales']
file = db['csv_files']

def file_h():    
    try:
        with open("file_1.csv") as file:
                lines = file.readlines()
                print("Extracting words...\n")
        for line in lines:
            word = line.split(",")
            print(word)
            print(type(word))       
       
        print ('\nfile read successfully\n')

    except Exception as e:
        print(e)
        file_h() 

from pymongo import MongoClient
from bson.objectid import ObjectId
file = db['csv_files']
def view_files():    
    try:
        client = MongoClient()
        db = client['tyrone_auto_sales']
        file = db['csv_files']
        results = file.find({},{"_id":0})
        for result in results:
            print(result)
            print(" ")

    except Exception as e:
        print(e) 
        view_files()    
      
              
menu()
option = int(input("\nEnter your option: "))

while option != 0:
    if option == 1:
        cars_view()
       
        
    elif option == 2:
        # View customers
        view_customers()

    elif option == 3:
        #insert car
        insert()
        
    elif option == 4:
        #delete car
        delete()
   
    elif option == 5:
        #new customer
        customers()

    elif option == 6:
        #Delete customer
        del_cust()    
        
    elif option == 7:
        #update
        update()   
    elif option == 8:
        # create cvs file
        file_h()   

    elif option == 9:
        # create cvs file
        view_files()      

    else:
        print("\nInvalid option.")
        
    print()
    menu()
    option = int(input("\nEnter your option: "))

print("\nThanks for using this program. Goodbye.")

