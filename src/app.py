"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db
from routes.user_routes import user_bp  # Importar el blueprint de user_routes
from routes.planet_routes import planet_bp  # Importar el blueprint de planet_routes
from routes.people_routes import people_bp  # Importar el blueprint de people_routes
from routes.vehicle_routes import vehicle_bp  # Importar el blueprint de vehicle_routes
from routes.favorites_routes import favorites_bp  # Importar el blueprint de favorites_routes

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Registrar el blueprint de user_routes
app.register_blueprint(user_bp)
app.register_blueprint(planet_bp)
app.register_blueprint(people_bp)
app.register_blueprint(vehicle_bp)
app.register_blueprint(favorites_bp)  # Registrar el blueprint de favorites_routes

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
