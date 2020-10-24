# Store_Simulator

This program is an online store simulator. It hase three classes: Product, Customer and Store.


**Product:**
A Product object represents a product with an ID code, title, description, price and quantity available. When the product is added to someone's cart the cost of the product will be added to the overall charge of the customer's cart. 


**Customer:**
A Customer object represents a customer with a name and account ID. Customers must be members of the Store to make a purchase. Premium members get free shipping which is calculatd at check out. Each customer will have a cart that will cointain every product that the customer has added into. This interacts with the store class to keep track of inventory. 


**Store:**
A Store object represents a store, which has some number of products in its inventory and some number of customers as members.
* A Store's inventory is a collection of Products that are part of the Store 
* A Store's membership is a collection of Customers that are members of the Store 
