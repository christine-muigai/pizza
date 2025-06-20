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

    
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({'error': 'Pizza or Restaurant not found'}), 404

    if not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    try:
        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create RestaurantPizza'}), 500

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


