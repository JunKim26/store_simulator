# Author: Jun Kim
# Date:04/07/2020
# Description: Program for an online store simulator.


# define class Product
class Product:
    """Represents private values of a product object"""

    def __init__(self,id,title,description,price,quantity):
        """initialize the Product with given parameters"""

        self._id = id
        self._title = title
        self._description = description
        self._price = price
        self._quantity = quantity


    def get_product_id(self):
        """Returns the ID"""
        return self._id

    def get_title(self):
        """Returns the title"""
        return self._title

    def get_description(self):
        """Returns the description"""
        return self._description

    def get_price(self):
        """Returns the price"""
        return self._price

    def get_quantity_available(self):
        """Returns the quantity"""
        return self._quantity

    def decrease_quantity(self):
        self._quantity -= 1


# define class Customer
class Customer:
    """Represents a customer with a name and account ID."""

    def __init__(self,name,customer_ID,premium_status):
        """initialize the Customer with given parameters"""

        self._name = name
        self._customer_ID = customer_ID
        self._premium_status = premium_status
        self._cart = []


    def get_name(self):
        """Returns the name"""
        return self._name

    def get_customer_id(self):
        """Returns the customer ID"""
        return self._customer_ID

    def is_premium_member(self):
        """Returns the premium status of member"""

        if self._premium_status == True:
            return True
        else:
            return False

    def get_cart(self):
        """Returns the cart"""
        return self._cart

    def add_product_to_cart(self,product):
        """adds a product into cart"""

        self._cart.append(product)

    def empty_cart(self):
        """clears cart into an empty set"""

        self._cart = []

class InvalidCheckoutError(Exception):
    """Exception for if customer ID does not match a customer in store during checkout"""
    pass

# define class Store
class Store:
    """Represents a store, which have a number of products in its inventory and customers as members."""

    def __init__(self):
        """initializes the Store inventory and members"""

        self._inventory = []
        self._members = []

    def get_inventory(self):
        """Returns the inventory"""
        return self._inventory

    def get_members(self):
        """Returns the members list"""
        return self._members

    def add_product(self,product_ID):
        """adds product object into inventory"""

        self._inventory.append(product_ID)

    def add_member(self,member_ID):
        """adds customer object to member list"""

        self._members.append(member_ID)

    def get_product_from_id(self,id):
        """Takes a Product ID and returns the Product object with the matching ID"""

        for product in self._inventory: # for loop to cycle through every product to find product with matching id

            if id == product.get_product_id():
                return product

            else:
                return None

    def get_member_from_id(self,id):
        """Takes a member ID and returns the customer object with the matching ID"""

        for member in self._members: # for loop to cycle through every members to find the matching id

            if id == member.get_customer_id:
                return member

            else:
                return None

    def product_search(self,string):
        """Takes a search string and returns a sorted list of ID codes"""

        # for every element in the inventory, if there is the string in either the title or description,
        # add the product ID into a list and return the sorted list

        matching_list = []

        for item in self._inventory:

            if string.lower() in str(item.get_title()).lower():
                matching_list.append(item.get_product_id())
            elif string.lower() in str(item.get_description()).lower():
                matching_list.append(item.get_product_id())

        return sorted(matching_list)


    def add_product_to_member_cart(self,productID,customerID):
        """adds product into customer's cart, assuming both member id and product id are valid and available"""

        for item in self._inventory: #checks through every product in inventory to find the respective product'

            if item.get_product_id() == productID: #if there is a matching product in the inventory

                for member in self._members: #checks through every memberID in members list to find the member

                    if member.get_customer_id() == customerID: #if there is a matching member in the list of members

                        if item.get_quantity_available() != 0:  #if there is at least one product quantity available

                            member.add_product_to_cart(item) # adds product into member's cart

        list_of_ids = []
        list_of_members = []

        for product in self._inventory:
            list_of_ids.append(product.get_product_id())

        for member in self._members:
            list_of_members.append(member.get_customer_id())

        if productID not in list_of_ids: #if there is no matching product in inventory, return statement
            return "product ID not found"

        if customerID not in list_of_members: #if there is no matching member in member list, return statement
            return "member ID not found"

        for item in self._inventory: #checks through every product in inventory to find the respective product'

            if item.get_product_id() == productID: #if there is a matching product in the inventory

                for member in self._members: #checks through every memberID in members list to find the member

                    if member.get_customer_id() == customerID: #if there is a matching member in the list of members

                        if item.get_quantity_available() == 0:  #if there is no quantity available

                            return "product out of stock"


    def check_out_member(self,customer_ID):
        """Checks out member and gives them the charge of the items in the cart if items were valid and available"""

        list_of_members_2 = []

        for member in self._members:
            list_of_members_2.append(member.get_customer_id())

        if customer_ID not in list_of_members_2: #condition for raising the exception error
            raise InvalidCheckoutError

        premium_charge = 0

        for item in member.get_cart(): #each product in cart

            if item.get_quantity_available != 0:  #checks availability of stock on product

                premium_charge += item.get_price()  #adds each products cost into charge

                item.decrease_quantity()

            else:
                continue


        for member in self._members:  # checks through every memberID in members list

            if member.get_customer_id() == customer_ID:  # if there is a matching member in the list of members

                member.empty_cart

                if member.is_premium_member() == True: #if member is premium member skip the shipping charge

                    return premium_charge

                else:

                    return premium_charge*1.07

def main():
    """main function that runs if file is run as script"""

    try:
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("890", "cat", "tony the tiger", 60, 3)
        p3 = Product("891", "dog", "clifford the big red dog", 20, 1)
        c1 = Customer("Yinsheng", "QWF", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product(p3)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        myStore.add_product_to_member_cart("890", "QWF")
        myStore.add_product_to_member_cart("891", "QWF")
        result = myStore.check_out_member("QWF")

        print (result)

    except InvalidCheckoutError:
        print("Customer ID does not match a member of the Store")


if __name__ == '__main__':
    main()