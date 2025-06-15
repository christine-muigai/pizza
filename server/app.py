from flask import Flask, jsonify
from flask_migrate import Migrate
from server.config import Config
from server.models import db
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app


app = create_app()


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Pizza Restaurant API"}), 200


if __name__ == '__main__':
    app.run(debug=True)
