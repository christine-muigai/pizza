# Pizza API Challenge

This is a simple RESTful API for a Pizza Restaurant built using **Flask**, **SQLAlchemy**, and **Flask-Migrate**. It allows you to manage restaurants, pizzas, and the association between them.

## Project Structure

pizza/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── models/
│ │ ├── init.py
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ └── controllers/
│ ├── restaurant_controller.py
│ ├── pizza_controller.py
│ └── restaurant_pizza_controller.py
├── migrations/
├── .venv/
├── .gitignore
└── README.md

yaml
Copy
Edit

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/christine-muigai/pizza.git
cd pizza-api
2. Set Up the Virtual Environment
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up the Database
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Run the Server
bash
Copy
Edit
flask run

API Endpoints
Restaurants
Method	Endpoint	Description
GET	/restaurants	Get all restaurants
GET	/restaurants/<id>	Get a specific restaurant
DELETE	/restaurants/<id>	Delete a restaurant

Pizzas
Method	Endpoint	Description
GET	/pizzas	Get all pizzas

Restaurant Pizzas
Method	Endpoint	Description
POST	/restaurant_pizzas	Create a pizza-restaurant relation

Example POST /restaurant_pizzas Body
json
Copy
Edit
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1
}

Postman Collection
A Postman collection is included for testing the endpoints.

If needed, import pizza_api_collection.json via Postman → Import → File.

.gitignore
Make sure .gitignore includes:

gitignore
Copy
Edit
.venv/
__pycache__/
*.pyc
instance/
.env