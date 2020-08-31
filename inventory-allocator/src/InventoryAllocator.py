"""
Marcos Hung

This class is used to implement the logic to process the input and return the desired output.
takes in two inputs: order and warehouse information.
"""

from warehouse import Warehouse

class InventoryAllocator:

	def __init__(self, order, warehouses):

		#order will be a map of item name : quantity
		self.order = order
		
		self.warehouses = self.parse_warehouses(warehouses)
	
	#creates warehouse objects from the data in the list for easier accessibility
	def parse_warehouses(self, warehouseList):
		result = []
		if not isinstance(warehouseList, list):
			raise TypeError("Input must be a list of dictionaries")
		for wh in warehouseList:
			if not isinstance(wh, dict):
				raise TypeError("List must contain dictionaries with name of warehouse mapped to its inventory")
			if not "name" in wh:
				raise ValueError("warehouse input must contain a name")
			if not "inventory" in wh:
				raise ValueError("warehouse input must contain an inventory")
			result.append(Warehouse(wh.get("name"), wh.get("inventory")))
		return result

	#searches warehouses to see if order can be fufilled and if so returns the warehouse shipping information in designated format
	def fufill_order(self):

		order_status = {}
		#traverse all orders
		for item in self.order:
			order_quantity = self.order.get(item)
			current_count = 0

			#look through all warehouses
			for warehouse in self.warehouses:
				remaining = order_quantity - current_count
				warehouse_amount = warehouse.find_order(item)

				#special case: warehouse has none of the item
				if warehouse_amount == 0:
					continue
				#special case: the amount in warehouse is more than necessary. Only take what we need
				if warehouse_amount > remaining:
					current_count += remaining
					warehouse_amount = remaining
					warehouse.subtract_inventory(item, remaining)
				else:
					current_count += warehouse_amount
					warehouse.subtract_inventory(item, warehouse_amount)
				if(warehouse.name in order_status):
					order_status[warehouse.name].append({item: warehouse_amount})
				else:
					order_status[warehouse.name] = [{item: warehouse_amount}]

				#no need to continue this traversal
				if(current_count == order_quantity):
					break
			#returns empty dict bc if one item can't be fufilled the whole order is cancelled
			if current_count < order_quantity:
				return {}

		return order_status