from flask import Blueprint, jsonify, request
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    
    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({'error': 'Missing required fields'}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    if not rp.validate():
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    db.session.add(rp)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza_id': rp.pizza_id,
        'restaurant_id': rp.restaurant_id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201
