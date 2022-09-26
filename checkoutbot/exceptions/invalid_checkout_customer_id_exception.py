class InvalidCustomerIdException(Exception):

	def __init__(self, exception):
		self.message = "Invalid customer_id provided. Check that customer_id is valid and that they have added items " \
					   "for checkout. "
		super().__init__(exception)

	def __str__(self):
		return f"{self.message}"
