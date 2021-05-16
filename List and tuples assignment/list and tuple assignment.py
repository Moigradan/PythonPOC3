# Hobby Shop
# Requirements:
# - Have at least 400 articles in the shop
# - Have at least four types of articles (shirt, scarf, glove, heat)
# - Have at least five sizes (S M L XL XXL) for each type of article
# - To be able to sell the latest article that was added to the shop
# - To be able to sell any item that is in the shop
# - To restock the shop with new items

def menu():
    while True: #allows user to make multiple choices of add/remove items from the best shop in the world everytime it runs a function

        print(''' 
        This is not the greatest shop in the world. This is just a tribute
        
        Press 1 to view store items - Over 400 items in stock ( not really )
        Press 2 in order to create a new stock item
        Press 3 to sell item
        ''')
        option = input("Select from the best shop in the world menu:  ") #User can press either 1, 2 or 3 on keyboard to call any function
        if option == "1":
            displayList()
        elif option == "2":
            addItem()
        elif option == "3":
            SellItem()

# storing products and their sizes in lists instead of tuples, so they can be added/removed by the user

products_list = ["Shirt", "Scarf", "Glove", "Jacket", "Boots", "Hat"]
products_list_size = ["XS", "S", "M", "L", "XL", "XXL"]

# function for displaying when called if user pressed 1

def displayList():
     for n, s in zip(products_list, products_list_size): # Zip function used to print out the product with its size
         print("Product: " + n, ", size: ", s)

# function for adding item when user pressed 2

def addItem():
    item = input("Enter the item you wish to add to product inventory: ")
    products_list.append(item)
    size = input("Enter the size of "+ item + ": ")
    products_list_size.append(size)
    print("Product " + item + " size " + size + " has been added and is now available for purchase")

def SellItem():
    item = input("What item do you wish to sell? ")
    if item in products_list: # checking if the selected item exists
        products_list.remove(item)
        print(item + " Has been selected")
    size = input("What size? ")
    if size in products_list_size: # if so, what about the size of the product?
        products_list_size.remove(size)
        print("Product " +item + " size " + size + " has been sold")
    else:
         print("Item does not exist")

menu() # menu is being called all the time