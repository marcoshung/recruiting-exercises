"""
Marcos Hung

This class represents the warehouse data structure that will be used to host the input data for convenience.
"""

class Warehouse:

	def __init__(self, name, inventory):
		self.name = name
		if not isinstance(inventory, dict):
			raise TypeError("inventory must be a dictonary value")
		self.inventory = inventory
	
	#This method returns all the necessary information to be used in the problem in the specified format as seen in the example inputs
	def get_warehouse_info(self):
		return {self.name, self.inventory}
	
	#returns the quantiity of the specified item if it exists
	def find_order(self, product):
		if product in self.inventory:
			return self.inventory.get(product)
		return 0

	#removes items from the warehouse
	def subtract_inventory(self, product, quantity):
		if not product in self.inventory:
			return
		if(quantity < 0):
			raise ValueError("Quantity to subtract must be greater than 0")
		if(quantity >= self.inventory.get(product)):
			self.inventory.pop(product, None)
		else:
			self.inventory[product] = self.inventory.get(product) - quantity
