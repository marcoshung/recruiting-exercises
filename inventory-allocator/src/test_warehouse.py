"""
Marcos Hung
Tests warehouses's methods and constructor with corner cases
"""

from InventoryAllocator import InventoryAllocator
import unittest
from InventoryAllocator import InventoryAllocator
from warehouse import Warehouse

#base warehouses to refer to for testing. These are not all Warehouses that will be tested
test_1 = Warehouse("test 1", {"apples" : 5})
test_2 = Warehouse("test 2", {"banana" :5 , "apples" :10, "pears": 7})
test_3 = Warehouse("test 3" ,{})

class TestWarehouse(unittest.TestCase):

    def test_warehouse_create(self):
        self.assertEqual(test_1.name, "test 1")
        self.assertEqual(test_1.inventory, {"apples" : 5})

        self.assertEqual(test_2.name, "test 2")
        self.assertEqual(test_2.inventory, {"banana" :5 , "apples" :10, "pears": 7})

        self.assertEqual(test_3.name, "test 3")
        self.assertEqual(test_3.inventory, {})

        with self.assertRaises(TypeError):
            Warehouse("invalid warehouse", 5)
        with self.assertRaises(TypeError):
            Warehouse("invalid warehouse", "string")


    def test_warehouse_find_orders(self):
        self.assertEqual(test_1.find_order("apples"), 5)
        self.assertEqual(test_1.find_order("Not found"), 0)

        self.assertEquals(test_3.find_order("apples"),0)

    def test_subtract_inventory(self):
        sub_test_1 = Warehouse("test 1", {"apples" : 5})
        sub_test_1.subtract_inventory("apples", 5)
        self.assertEqual(sub_test_1.find_order("apples"),0)
        
        sub_test_2 = Warehouse("test 2", {"banana" :5 , "apples" :10, "pears": 7})
        sub_test_2.subtract_inventory("banana", 3)
        self.assertEqual(sub_test_2.find_order("banana"), 2)
        sub_test_2.subtract_inventory("apples", 15)
        self.assertEqual(sub_test_2.find_order("apples"), 0)
        self.assertEqual(sub_test_2.subtract_inventory("Not found", 5), None)

        with self.assertRaises(ValueError):
            sub_test_2.subtract_inventory("banana", -5)

if __name__ == "__main__":
    unittest.main()