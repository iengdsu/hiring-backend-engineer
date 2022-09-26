from typing import Dict

from entities import RegisterType
from exceptions.invalid_checkout_customer_id_exception import InvalidCustomerIdException


class StoreModel:
	"""
	Class that maintains the state of customers adding items to registers and checking out.

	* next: int
	Represents the next open register the customer will be assigned to. Increments linearly

	* registers: Map<register_id, List[item_id]>
	A Map of register_id's and a list of item_id's at that register. Default of 25 registers.

	* customer_register: Map<customer_id, register_id>
	Tracks customer_id and their assigned register_id
	"""

	def __init__(self):
		self.next = 0
		self.registers: RegisterType = {i: [] for i in range(0, 25)}
		self.customer_register: Dict[int, int] = {}

	def get_next_register(self) -> int:
		"""
		Returns the next register_id that a new customer will be sent to
		:return: int
		"""
		if self.next > 24:
			self.next = 0
		next = self.next
		self.next += 1
		return next

	def clear(self) -> None:
		"""
		Reset StoreModel back to it's initial state
		:return: void
		"""
		self.next = 0
		self.registers: RegisterType = {i: [] for i in range(0, 25)}
		self.customer_register: Dict[int, int] = {}

	def checkout(self, customer_id: int) -> None:
		"""
		Clears all customer_id items from the assigned register.
		:param customer_id: int
		:return:
		"""
		try:
			register_id = self.customer_register[customer_id]
			del self.customer_register[customer_id]
			self.registers[register_id] = []
		except KeyError as e:
			print("KeyError: " + str(e))
			print("customer_id: " + str(customer_id))
			raise InvalidCustomerIdException(e)

	def get_assigned_register(self, customer_id: int) -> int:
		if customer_id in self.customer_register:
			register_id = self.customer_register[customer_id]
		else:
			register_id = self.get_next_register()
			self.customer_register[customer_id] = register_id
		return register_id
