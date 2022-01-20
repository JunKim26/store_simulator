# Author: Jun Kim
# Date:04/07/2020
# Description: 5 unittests for the Store.py program.

import unittest

from Store import Product, Customer, InvalidCheckoutError, Store

class TestProjects(unittest.TestCase):
    """defines unit tests for store project"""

    def test_1(self):

        p1 = Product("111", "Orange Juice", "Off Brand OJ with pulp", 3.99, 3)
        c1 = Customer("Jun", "ABC", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("111", "ABC")
        result = myStore.check_out_member("ABC")

        self.assertTrue(c1.is_premium_member())

    def test_2(self):

        p1 = Product("111", "Orange Juice", "Off Brand OJ with pulp", 3.99, 3)
        c1 = Customer("Jun", "ABC", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("111", "ABC")
        result = myStore.check_out_member("ABC")

        self.assertAlmostEqual(result,3.99)

    def test_3(self):
        p1 = Product("112", "Milk", "2% Milk fat", 2.00, 7)
        p2 = Product("113", "Toilet Paper", "To wipe away the coronavirus", 100.00, 7)
        c1 = Customer("Jun", "ABC", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("112", "ABC")
        myStore.add_product_to_member_cart("113", "ABC")
        result = myStore.check_out_member("ABC")
        self.assertAlmostEqual(result,102.00)

    def test_4(self):
        with self.assertRaises(InvalidCheckoutError):
            p1 = Product("111", "Orange Juice", "Off Brand OJ with pulp", 3.99, 3)
            c1 = Customer("Jun", "ABC", True)
            myStore = Store()
            myStore.add_product(p1)
            myStore.add_member(c1)
            myStore.add_product_to_member_cart("111", "ABC")
            result = myStore.check_out_member("ABD")

    def test_5(self):
        p1 = Product("111", "Orange Juice", "Off Brand OJ with pulp", 3.99, 3)
        c1 = Customer("Jun", "ABC", False)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("111", "ABC")
        result = myStore.check_out_member("ABC")

        self.assertFalse(c1.is_premium_member())

if __name__ == '__main__':
    unittest.main()
