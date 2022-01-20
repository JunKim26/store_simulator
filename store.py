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

    def add_product(self,product):
        """adds product ID into inventory"""

        self._inventory.append(product)

    def add_member(self,member):
        """adds customer ID to member list"""

        self._members.append(member)

    def get_product_from_id(self,id):
        """Takes a Product ID and returns the Product object with the matching ID"""

        if self._inventory == []:
            return None

        for product in self._inventory: # for loop to cycle through every product to find product with matching id


            if id == product.get_product_id():
                return product

        else:
            return None

    def get_member_from_id(self,id):
        """Takes a member ID and returns the customer object with the matching ID"""

        if self._members == []:
            return None

        for member in self._members: # for loop to cycle through every members to find the matching id

            if id == member.get_customer_id():
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

        product = self.get_product_from_id(productID)
        member = self.get_member_from_id(customerID)

        if product == None:
            return "product ID not found"

        if member == None:
            return "member ID not found"

        if product.get_quantity_available() == 0:
            return "product out of stock"


        member.add_product_to_cart(product) # adds product into member's cart

        return "product added to cart"


    def check_out_member(self,customer_ID):
        """Checks out member and gives them the charge of the items in the cart if items were valid and available"""

        list_of_members_id = []

        for member in self._members:
            list_of_members_id.append(member.get_customer_id())

        if customer_ID not in list_of_members_id: #if customer is not a member, raise error
            raise InvalidCheckoutError

        member = self.get_member_from_id(customer_ID)

        premium_charge = 0

        for item in member.get_cart(): #each product in cart

            if item.get_quantity_available() != 0:  #checks availability of stock on product

                premium_charge += item.get_price()  #adds each products cost into charge

                item.decrease_quantity()

            else:
                continue

        member.empty_cart()

        if member.is_premium_member() == True: #if member is premium member skip the shipping charge

            return premium_charge

        else:

            return premium_charge*1.07

def main():
    """main function that runs if file is run as script"""

    try:
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33, 1)
        p2 = Product("890", "cat", "tony the tiger", 60, 1)
        p3 = Product("891", "dog", "clifford the big red dog", 20, 1)
        c1 = Customer("Yinsheng", "QWF", True)
        c2 = Customer("David", "QLR", False)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product(p3)
        myStore.add_member(c1)
        myStore.add_member(c2)
        myStore.add_product_to_member_cart("889", "QWF")
        myStore.add_product_to_member_cart("890", "QWF")
        myStore.add_product_to_member_cart("889", "QLR")
        myStore.add_product_to_member_cart("891", "QLR")
        result1 = myStore.check_out_member("QWF")
        result2 = myStore.check_out_member("QLR")

        print (result1)
        print (result2)

    except InvalidCheckoutError:
        print("Customer ID does not match a member of the Store")


if __name__ == '__main__':
    main()
