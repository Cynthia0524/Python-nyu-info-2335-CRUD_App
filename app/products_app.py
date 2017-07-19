import csv

username = input("Please input your username: ")

products_path = "/Users/cynthia/Desktop/Github/Python-nyu-info-2335-CRUD_App/data/products.csv"
products = []
keys = ["id","name","aisle","department","price"]
with open(products_path, "r") as products_file:
    reader = csv.DictReader(products_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        dic = dict.fromkeys(keys)
        for key in keys:
            dic[key] = row[key]
        products.append(dic)
#        products.append({"id":row["id"],"name":row["name"],"aisle":row["aisle"],"department":row["department"],"price":row["price"]})

def look_up_id(id):
    match = [product for product in products if product["id"] == id]
    return match[0]

#print("-------------------------------")
#print("PRODUCTS APPLICATION")
#print("-------------------------------")
print("\n" + "-------------------------------" + "\n" + "PRODUCTS APPLICATION" + "\n" + "-------------------------------")
print("Welcome @" + username + "!")
print("\n")

def operation_guide():
    print("\n")
    print("There are " + str(len(products)) + " products in the database. Please select an operation: ")
    print("\n")
    print("    operation | description")
    print("    --------- | ------------------")
    print("    'List'    | Display a list of product identifiers and names.")
    print("    'Show'    | Show information about a product.")
    print("    'Create'  | Add a new product.")
    print("    'Update'  | Edit an existing product.")
    print("    'Destroy' | Delete an existing product.")
    print("\n")

operation_guide()

operation = input(" ")

while True:

    if operation == "List":
        print("THERE ARE " + str(len(products)) + " PRODUCTS:")
        for product in products:
            print("  + " + str(product))

        choice = input("\nDo you want to continue?\n'Yes' for guide\n'No' for exit\nOr directly input your operation choice: ")
        if choice == "Yes":
            operation_guide()
            operation = input(" ")
        elif choice in ["List","Show","Create","Update","Destroy"]: operation = choice
        else: operation = "Exit"


    elif operation == "Show":
        show_id = input("OK. Please specify the product's identifier: ")
        ids = []
        for product in products:
            ids.append(product["id"])
        while(show_id not in ids):
            show_id = input("Wrong identifier! Please try again: ")
        print("SHOWING A PRODUCT HERE!")
        print(str(look_up_id(show_id)))

        choice = input("\nDo you want to continue?\n'Yes' for guide\n'No' for exit\nOr directly input your operation choice: ")
        if choice == "Yes":
            operation_guide()
            operation = input(" ")
        elif choice in ["List","Show","Create","Update","Destroy"]: operation = choice
        else: operation = "Exit"


    elif operation == "Create":
        print("OK. Please specify the product's information...")
        def greatest_id(products):
            ids = []
            for product in products:
                ids.append(int(product["id"]))
            return max(ids)
        new_product = dict.fromkeys(keys)
        new_product["id"] = str(greatest_id(products)+1)
        for key in keys[1:]:
            new_product[key] = input("    "+key+": ")
        print("CREATING A PRODUCT HERE!")
        print(new_product)
        print("\n")
        products.append(new_product)
#        with open(products_path, "a", newline='') as products_file:
#            writer = csv.DictWriter(products_file,fieldnames = keys)
#            new_row = csv.writer(products_file)
#            new_row.writerow("")
#            writer.writerow(new_product)

        choice = input("\nDo you want to continue?\n'Yes' for guide\n'No' for exit\nOr directly input your operation choice: ")
        if choice == "Yes":
            operation_guide()
            operation = input(" ")
        elif choice in ["List","Show","Create","Update","Destroy"]: operation = choice
        else: operation = "Exit"


    elif operation == "Update":
        update_product = dict.fromkeys(keys)
        update_product["id"] = input("OK. Please specify the product's identifier: ")
        ids = []
        for product in products:
            ids.append(product["id"])
        while(update_product["id"] not in ids):
            update_product["id"] = input("Wrong identifier! Please try again: ")
        print("OK. Please specify the product's information...")
        for key in keys[1:]:
            update_product[key] = input("    Change "+key+" from "+"'"+look_up_id(update_product["id"])[key]+"'"+" to: ")
        print("UPDATING A PRODUCT HERE!")
        print(update_product)
        for product in products:
            if product["id"] == update_product["id"]:
                index = products.index(product)
                products[index] = update_product

        choice = input("\nDo you want to continue?\n'Yes' for guide\n'No' for exit\nOr directly input your operation choice: ")
        if choice == "Yes":
            operation_guide()
            operation = input(" ")
        elif choice in ["List","Show","Create","Update","Destroy"]: operation = choice
        else: operation = "Exit"


    elif operation == "Destroy":
        destroy_id = input("OK. Please specify the product's identifier: ")
        ids = []
        for product in products:
            ids.append(product["id"])
        while(destroy_id not in ids):
            destroy_id = input("Wrong identifier! Please try again: ")
        print("DESTROYING A PRODUCT HERE!")
        print(look_up_id(destroy_id))
        for product in products:
            if product["id"] == destroy_id:
                index = products.index(product)
                del products[index]

        choice = input("\nDo you want to continue?\n'Yes' for guide\n'No' for exit\nOr directly input your operation choice: ")
        if choice == "Yes":
            operation_guide()
            operation = input(" ")
        elif choice in ["List","Show","Create","Update","Destroy"]: operation = choice
        else: operation = "Exit"


    elif operation == "Exit":
        with open(products_path, "w") as products_file:
            writer = csv.DictWriter(products_file, fieldnames=["id", "name", "aisle", "department", "price"])
            writer.writeheader() # uses fieldnames set above
            for i in products:
                writer.writerow(i)
        break


    else:
        operation = input("Wrong input! Please try again: ")
        print("\n")
