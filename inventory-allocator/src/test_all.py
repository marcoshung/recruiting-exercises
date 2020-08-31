"""
Marcos Hung
file to run all test cases
"""
import unittest
from test_InventoryAllocator import TestInventoryAllocator
from test_warehouse import TestWarehouse

def create_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestInventoryAllocator))
	suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestWarehouse))

	return suite

if __name__ == "__main__":
	suite = create_suite()
	unittest.TextTestRunner().run(suite)