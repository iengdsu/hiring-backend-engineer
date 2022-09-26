from flask import Flask, request, make_response

from activity.add_activity import AddActivity
from activity.checkout_activity import CheckoutActivity
from models.store_model import StoreModel

app = Flask(__name__)
store = StoreModel()


@app.route("/health", methods=["GET"])
def health_check():
    return "200"


@app.route("/state", methods=["DELETE"])
def clear_all_registers():
    store.clear()
    return "204"


@app.route("/add", methods=["POST"])
def add_event():
    add_data = AddActivity.add_item_to_register(request.form, store)
    response = make_response(add_data, "201")
    return response


@app.route("/checkout", methods=["POST"])
def checkout_event():
    CheckoutActivity.checkout(request.form, store)
    return "201"


if __name__ == "__main__":
    app.run(debug=True)
