from models.store_model import StoreModel
from typing import Dict, List


class AddActivity:

	@staticmethod
	def add_item_to_register(data, store: StoreModel) -> Dict[str, Dict[int, List[int]]]:
		customer_id = int(data.get("customer_id"))
		item_id = int(data.get("item_id"))
		register_id = store.get_assigned_register(customer_id)

		registers_wrapper = {"registers": store.registers}
		store.registers[register_id].append(item_id)
		return registers_wrapper
