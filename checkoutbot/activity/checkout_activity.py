from models.store_model import StoreModel


class CheckoutActivity:

	@staticmethod
	def checkout(data, store: StoreModel) -> None:
		customer_id = int(data.get("customer_id"))
		store.checkout(customer_id)
