"""
Marcos Hung
Tests InventoryAllocator's methods and constructor with corner cases
"""

import unittest
import copy
from InventoryAllocator import InventoryAllocator
from warehouse import Warehouse

#base warehouses inputs to refer to for testing. These are not all Warehouses that will be tested

test_wh_1 = {"name":"test 1","inventory": {"apples" : 5}}
test_wh_2 = {"name":"test 2", "inventory": {"banana" :5 , "apples" :10, "pears": 7}}
test_wh_3 = {"name":"test 3" ,"inventory": {}}
test_wh_4 = {"name":"test 4", "inventory": {"banana" :7, "pears" : 3, "oranges":2}}

#base InventoryAllocators  to refer to for testing. These are not all InventoryAllocators that will be tested

test_IA_1 = InventoryAllocator({"apples" :5}, [test_wh_1, test_wh_2, test_wh_4])
test_IA_2 = InventoryAllocator({"apples" :9}, [test_wh_1, test_wh_2, test_wh_4])
test_IA_3 = InventoryAllocator({"apples" :7, "banana": 2,"oranges" :10}, [test_wh_1, test_wh_2, test_wh_4])
test_IA_4 = InventoryAllocator({"apples" :5}, [test_wh_3])

class TestInventoryAllocator(unittest.TestCase):

	def test_parse_warehouses(self):
		#tests valid input and makes sure values are what is expected
		parse_test = InventoryAllocator.parse_warehouses(self,[test_wh_1,test_wh_2,test_wh_3, test_wh_4])
		for wh in parse_test:
			self.assertIsInstance(wh, Warehouse)
		self.assertEqual(parse_test[0].name, "test 1")
		self.assertEqual(parse_test[0].inventory, {"apples" : 5})
		self.assertEqual(parse_test[1].name, "test 2")
		self.assertEqual(parse_test[1].inventory, {"banana" :5 , "apples" :10, "pears": 7})
		self.assertEqual(parse_test[2].name, "test 3")
		self.assertEqual(parse_test[2].inventory, {})
		self.assertEqual(parse_test[3].name, "test 4")
		self.assertEqual(parse_test[3].inventory, {"banana" :7, "pears" : 3, "oranges":2})

		#test invalid inputs
		with self.assertRaises(TypeError):
			InventoryAllocator.parse_warehouses(self, "wrong input")
		with self.assertRaises(TypeError):
			InventoryAllocator.parse_warehouses(self, ["wrong", "input", "still"])

	def test_create_IA(self):
		
		self.assertEqual(test_IA_1.order,{"apples" :5})
		self.assertEqual(len(test_IA_1.warehouses), 3)

		self.assertEqual(test_IA_2.order, {"apples" :9})
		self.assertEqual(len(test_IA_2.warehouses), 3)

		self.assertEqual(test_IA_3.order, {"apples" :7, "banana": 2,"oranges" :10})
		self.assertEqual(len(test_IA_3.warehouses), 3)

		self.assertEqual(test_IA_4.order, {"apples" :5})
		self.assertEqual(len(test_IA_4.warehouses), 1)
		
	def test_fufill_order(self):
		order_test_1 = copy.deepcopy(test_IA_1)
		self.assertEqual(order_test_1.fufill_order(), {"test 1" :[{"apples":5}]})
		
		order_test_2 = copy.deepcopy(test_IA_2)
		self.assertEqual(order_test_2.fufill_order(), {"test 1" :[{"apples" :5}], "test 2" : [{"apples": 4}]} )

		order_test_3 = copy.deepcopy(test_IA_3)
		self.assertEqual(order_test_3.fufill_order(), {} )

		order_test_4 = copy.deepcopy(test_IA_4)
		self.assertEqual(order_test_4.fufill_order(), {})

		order_test_5 = InventoryAllocator({"apple": 1 }, [{ "name": "owd", "inventory": { "apple": 1 } }])
		self.assertEqual(order_test_5.fufill_order(), { "owd": [{ "apple": 1 } ]})

		order_test_6 = InventoryAllocator({ "apple": 10 }, [{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 }}])
		self.assertEqual(order_test_6.fufill_order(), { "dm": [{ "apple": 5 }],  "owd": [{ "apple": 5 }] })

		order_test_7 = InventoryAllocator({"apple" : 7, "orange" : 8, "pear" : 3}, 
									[{"name" : "wh1", "inventory":{"apple" : 5, "orange":3}},
									{"name" :"wh2", "inventory": {"apple" : 2, "orange" : 8}},
									{"name" : "wh3", "inventory" : {"pear" : 5}}
										])
		self.assertEqual(order_test_7.fufill_order(), 
					{"wh1": [{"apple":5}, {"orange":3}], 
					"wh2": [{"apple":2}, {"orange" : 5}],
					"wh3": [{"pear": 3}]})

if __name__ == "__main__":
	unittest.main()