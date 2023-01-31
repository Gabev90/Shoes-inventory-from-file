
#========The beginning of the class==========
class Shoe:
    #This is the initialise of the Shoe class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    
    #This method returns the "cost" of the product 
    def get_cost(self):
        return self.cost
    

    #This method returns the "quantity" of the product 
    def get_quantity(self):
        return self.quantity
    

    #This method returns a string representation of the class.
    def __str__(self):
        return f"""-------------------------------------------------------
        Country of origin:\t {self.country}
        Code of product:\t {self.code}
        Name of product:\t {self.product}
        Cost of product:\t {self.cost}
        Quantity of product:\t {self.quantity}
-------------------------------------------------------"""


#=============Shoe list===========
# This is the empty list where we will store the shoes objects from the "inventory.txt" file
shoe_list = []


#==========Functions outside the class==============
# This function will read in the "inventory.txt".
# At the try, if the file exist, then the for loop will strip and split the lines (first line skiped) and will store the shoes and objects in the empt list (shoe_list)
# at the except the program will print the message if the "inventory.txt" does no exist
def read_shoes_data():
    try:
        file = open("inventory.txt", "r")
        lines = file.readlines()
        file.close()

        for line in lines[1:]:
            data = line.strip()
            data = data.split(",")
            shoes = Shoe(country= data[0], code= data[1], product= data[2], cost= data[3], quantity= data[4])
            shoe_list.append(shoes)
        return
    
    except FileNotFoundError as error:
            print("\nThe file that you are trying to open does not exist")
            print(error)

                
#This function lets the user to add a new product to the list. (if the "inventory.txt" not opened yet, the program will ask the user to run the "read" menu first)
def capture_shoes():
    if len(shoe_list) == 0 :
        print("The list is empty! Please, run the 'read' first!")
    else:
        country = input("Please, enter the country of origin: ")
        code = input("Please, enter code of the product: ")
        product = input("Please, enter the name of the product: ")
        cost = input("Please, enter the cost of the product: ")
        quantity = input("Please, enter the quantity of the product: ")
        new_shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(new_shoe)
        print("New product is successfully added!")


#This function print out all the objects from the "shoe_list" (if the "inventory.txt" not opened yet, the program will ask the user to run the "read" menu first)
def view_all():
    if len(shoe_list) == 0 :
        print("The list is empty! Please, run the 'read' first!")
    else:
        for number in range(len(shoe_list)):
            print(shoe_list[number])
        return
    
    
# This funtion stores the quantities of shoes in the "quantity_list" then it checks the lowest number of the list and find the index of the lowest number in the list.
# With the indexnumber the program will print out the actual shoes with the lowest stock and ask the user if He/She wants to add to the stock.
# If the user wants to add to the stock. The program will ask for the number which will be given to the actual stock.
# Finally the code will changes the stock value of the shoes in the "shoe_list"
#(if the "inventory.txt" not opened yet, the program will ask the user to run the "read" menu first)
def re_stock():
    if len(shoe_list) == 0 :
        print("The list is empty! Please, run the 'read' first!")
    else:
        quantity_list = []
        for shoe in shoe_list:
            quantity_list.append(int(shoe.quantity))
    
        low_quant = min(quantity_list)
        low_quant_index = quantity_list.index(low_quant)
        print(f"""\nThe shoes with lowest quantity on stock:
{shoe_list[low_quant_index]}""")
    
        options = input("Do you want to add to this stock('yes' or 'no'): ")
        if options.lower() == "yes":
            while True:
                try:
                    volume = int(input("Enter the number which you want to add to stock: "))
                    for shoe in shoe_list:
                        if shoe == shoe_list[low_quant_index]:
                            shoe.quantity = int(shoe.quantity) + volume
                    print("New stock successfully added!")
                    break
                except ValueError:
                    print("The entered value is not a number!")
        elif options.lower() == "no":
            return
        else:
            print("Invalid option!")

        
# (if the "inventory.txt" not opened yet, the program will ask the user to run the "read" menu first)
# This function ask for a code from the user. If the code is valid, the code will print out the shoes, if the code is not in the list, the program returns to the main menu.
def seach_shoe():
    if len(shoe_list) == 0 :
        print("The list is empty! Please, run the 'read' first!")
    else:
        code = input("Please, enter the code: ")
        for shoe in shoe_list:
            if shoe.code == code:
                print(shoe)
                return
        


# (if the "inventory.txt" not opened yet, the program will ask the user to run the "read" menu first)
# This function will calls the "get_quantity" and "get_cost" methods from the "Shoe class".
# The program will use the quantity and cost the calculate the value and prints out the name, code, quantity, cost and the total value of each object in the "shoe_list"
def value_per_item():
    if len(shoe_list) == 0 :
        print("The list is empty! Please, run the 'read' first!")
    else:
        for shoe in shoe_list:
            quantity = int(Shoe(shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity).get_quantity())
            cost = int(Shoe(shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity).get_cost())
            print(f"""**************************************************
Name: \t\t{shoe.product}
Code: \t\t{shoe.code}
Quantity: \t{quantity}
Cost: \t\t{cost}
________________________
Total value: \t{quantity * cost}
**************************************************""")
        return
    


# (if the "inventory.txt" not opened yet, the program will ask the user to run the "read" menu first)
# This function stores the quantities of each shoes on the list and check the highest number on this list and checks the index of it on the list.
# Based on the list the program will prints out the correct shoes with the highest stock number with a "FOR SALE!!!" frame.
def highest_qty():
    if len(shoe_list) == 0 :
        print("The list is empty! Please, run the 'read' first!")
    else:
        quantity_list = []
        for shoe in shoe_list:
            quantity_list.append(int(shoe.quantity))
    
        max_quant = max(quantity_list)
        max_quant_index = quantity_list.index(max_quant)
    
        print(f"""\nThe shoes with highest quantity on stock:
FOR SALE!!!  FOR SALE!!!  FOR SALE!!!  FOR SALE!!!  FOR SALE!!! 
{shoe_list[max_quant_index]}
FOR SALE!!!  FOR SALE!!!  FOR SALE!!!  FOR SALE!!!  FOR SALE!!!""")
        return
    


#==========Main Menu=============
#At this part the menu will be printed out where the user can make his/her choice which menu to open.
while True:
    menu = input('''--------------------------------------------------------------------
Select one of the following Options below:
\tread  - Read data from file
\tnew   - Adding a new product
\tview  - View all products
\tstock - Lowest shoes on stock 
\tsearch- Search by code
\tvalue - Value of each item
\thigh  - Highest quantity on stock
\texit  - Exit
--------------------------------------------------------------------
: ''').lower()
    
    
    #At this part the menu options will call the correct function.
    if menu == 'read':
        read_shoes_data()
        print("data successfully read in.")

    elif menu == 'new':
        capture_shoes()
        
    elif menu == 'view':
        view_all()

    elif menu == 'stock':
        re_stock()

    elif menu == 'search':
        seach_shoe()
    
    elif menu == 'value':
        value_per_item()
    
    elif menu == 'high':
        highest_qty()

    elif menu == 'exit':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")