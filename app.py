import json
import random

from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per day"]
)


with open('data/bot-says.json') as f:
    data = json.load(f)

categories = data['categories']
orders = data['orders']


@app.route("/")
def index():

    greeting = [
        "Welcome to ChatGPT Says!",
        "Train for the the AI uprising by following ChatGPTs orders.",
        "Usage:",
        "       /bot-says",
        "       /bot-says?category=humorous&limit=5"
    ]
    return '\n'.join(greeting)


@app.route('/bot-says', methods=['GET'])
def bot_gets():
    if request.method == 'GET':

        order_id = request.args.get('id')
        category = request.args.get('category')
        limit = request.args.get('limit')
        filtered_orders = orders

        # if category return only category orders
        if category is not None:
            # get category name without '-'
            cat_name = " ".join(word.capitalize()
                                for word in category.split("-"))
            filtered_orders = [
                order for order in orders if order['category']['name'] == cat_name]

        # get number of orders to return
        if order_id is None:
            if limit == 'all':
                random_orders = filtered_orders
            else:
                if limit is not None:
                    num_orders = min(int(limit), len(filtered_orders))
                else:
                    num_orders = 1

                # select random orders
                random_orders = random.sample(filtered_orders, num_orders)

        # get order of order_id
        else:
            try:
                random_orders = [
                    order for order in orders if order['id'] == int(order_id)]
            except:
                return f"No order with id {order_id}. Usage: bot-says?id=4"

        response = random_orders[0] if len(
            random_orders) == 1 else random_orders

        return jsonify(response)


if __name__ == "__main__":
    app.run()
