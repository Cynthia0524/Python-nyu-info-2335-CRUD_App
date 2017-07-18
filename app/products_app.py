import csv

username = input("Please input your username: ")

products_path = "/Users/cynthia/Desktop/Github/Python-nyu-info-2335-CRUD_App/data/products.csv"
products = []
with open(products_path, "r") as products_file:
    reader = csv.DictReader(products_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        products.append({"id":row["id"],"name":row["name"],"aisle":row["aisle"],"department":row["department"],"price":row["price"]})

def look_up_id(id):
    match = [product for product in products if product["id"] == id]
    return match[0]

#print("-------------------------------")
#print("PRODUCTS APPLICATION")
#print("-------------------------------")
print("\n" + "-------------------------------" + "\n" + "PRODUCTS APPLICATION" + "\n" + "-------------------------------")
print("Welcome @" + username + "!")
print("\n")
print("There are " + str(len(products)) + " products in the database. Please select an operation: ")
print("\n")
print("    operation | description")
print("    --------- | ------------------")
print("    'List'    | Display a list of product identifiers and names.")
print("    'Show'    | Show information about a product.")
print("    'Create'  | Add a new product.")
print("    'Update'  | Edit an existing product.")
print("    'Destroy' | Delete and existing product.")
print("\n")

operation = input(" ")

if operation == "List":
    print("THERE ARE " + str(len(products)) + " PRODUCTS:")
    for product in products:
        print("  + " + str(product))

if operation == "Show":
    show_id = input("OK. Please specify the product's identifier: ")
    print("SHOWING A PRODUCT HERE!")
    print(str(look_up_id(show_id)))
