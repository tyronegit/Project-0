
# from click import option


# def menu():
#     print("[1] Option 1")
#     print("[2] Option 2")
#     print("[0] Exit the program.")

# menu()
# option = int(input("\nEnter your option: "))

# while option != 0:
#     if option == 1:
#         #do option 1 stuff
#         print("\nOption 1 has been called.")
#     elif option == 2:
#         #do option 2 stuff
#         print("\nOption 2 has been called.")
#     else:
#         print("\nInvalid option.")
#     print()
#     menu()
#     option = int(input("\nEnter your option: "))

# print("\nThanks for using this program. Goodbye.")

def menu():
    print("[1] view cars available")
    print("[2] View customers who purchased cars")
    print("[3] Place an Order")
    print("[4] View Orders for a Customer")
    print("[5] Create new customer")
    print("[6] Create new Product")
    print("[7] Delete an order")
    print("[8] Update customer details")
    print("[0] Exit")    

# print("View Products")
from pymongo import MongoClient
import datetime
from pprint import pprint

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
        print ('\nInserted data successfully\n')

    except Exception as e:
        print(e)


menu()
option = int(input("\nEnter your option: "))

while option != 0:
    if option == 1:
        # Load data if necessary
        # print("\nLoad Data called.")
        from pymongo import MongoClient
        from bson.objectid import ObjectId
        import datetime
        from pprint import pprint

        client = MongoClient()
        db = client['tyrone_auto_sales']
        cars = db['cars']
        results = cars.find({},{"_id":0})
        for result in results:
            pprint(result)
        
    elif option == 2:
        # # View customers
        # print("View Customers")
        from pymongo import MongoClient
        import datetime
        from pprint import pprint3

        client = MongoClient()
        db = client['tyrone_auto_sales']
        customers = db['customers']
        results = customers.find()
        for result in results:
            pprint(result)

    elif option == 3:
        #View customers
        insert()
    elif option == 4:
        #View customers
        print("Place an Order")
        pass
    elif option == 5:
        #View customers
        print("View Orders for a Customer")  
        pass   
    elif option == 6:
        #View customers
        print("Create new customer")  
        pass   
    elif option == 7:
        #View customers
        print("Create new Product")
        pass
    elif option == 8:
        #View customers
        print("Delete an order")  
        pass     
    elif option == 9:
        #View customers
        print("Update customer details")  
        pass   
    else:
        print("\nInvalid option.")
        
    print()
    menu()
    option = int(input("\nEnter your option: "))

print("\nThanks for using this program. Goodbye.")


# Function to insert data into mongo db


     
        
        










    
# 1. Load Data
# 2. View customers
# 3. View Products
# 4. Place an Order
# 5. View Orders for a Customer
# 6. Create new customer
# 7. Create new Product
# 8. Delete an order
# 9. Update customer details
# 0. Exit
