from flask import Blueprint, request, jsonify, g
from models import db, User, People, Planet, Vehicle

favorites_bp = Blueprint('favorites_bp', __name__)

# Decorador para obtener el user_id del usuario actualmente registrado/activo
def get_current_user():
    # Aquí deberías implementar la lógica para obtener el user_id del usuario actualmente registrado/activo
    # Por ejemplo, podrías obtenerlo de un token JWT o de la sesión
    # En este ejemplo, simplemente lo asignamos manualmente para ilustrar
    g.user_id = 1  # Reemplaza esto con la lógica real para obtener el user_id

@favorites_bp.before_request
def before_request():
    get_current_user()

@favorites_bp.route('/user/favorites', methods=['GET'])
def get_favorites():
    user = User.query.get(g.user_id)
    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    favorites = {
        "people": [people.serialize() for people in user.favorite_people],
        "planets": [planet.serialize() for planet in user.favorite_planets],
        "vehicles": [vehicle.serialize() for vehicle in user.favorite_vehicles]
    }

    return jsonify(favorites), 200

@favorites_bp.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user = User.query.get(g.user_id)
    people = People.query.get(people_id)

    if not user or not people:
        return jsonify({"msg": "Usuario o persona no encontrado"}), 404

    if people in user.favorite_people:
        return jsonify({"msg": "La persona ya está en favoritos"}), 400

    user.favorite_people.append(people)
    db.session.commit()

    return jsonify({"msg": "Persona añadida a favoritos"}), 200

@favorites_bp.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user = User.query.get(g.user_id)
    planet = Planet.query.get(planet_id)

    if not user or not planet:
        return jsonify({"msg": "Usuario o planeta no encontrado"}), 404

    if planet in user.favorite_planets:
        return jsonify({"msg": "El planeta ya está en favoritos"}), 400

    user.favorite_planets.append(planet)
    db.session.commit()

    return jsonify({"msg": "Planeta añadido a favoritos"}), 200

@favorites_bp.route('/favorite/vehicle/<int:vehicle_id>', methods=['POST'])
def add_favorite_vehicle(vehicle_id):
    user = User.query.get(g.user_id)
    vehicle = Vehicle.query.get(vehicle_id)

    if not user or not vehicle:
        return jsonify({"msg": "Usuario o vehículo no encontrado"}), 404

    if vehicle in user.favorite_vehicles:
        return jsonify({"msg": "El vehículo ya está en favoritos"}), 400

    user.favorite_vehicles.append(vehicle)
    db.session.commit()

    return jsonify({"msg": "Vehículo añadido a favoritos"}), 200

@favorites_bp.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    user = User.query.get(g.user_id)
    people = People.query.get(people_id)

    if not user or not people:
        return jsonify({"msg": "Usuario o persona no encontrado"}), 404

    if people not in user.favorite_people:
        return jsonify({"msg": "La persona no está en favoritos"}), 400

    user.favorite_people.remove(people)
    db.session.commit()

    return jsonify({"msg": "Persona eliminada de favoritos"}), 200

@favorites_bp.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user = User.query.get(g.user_id)
    planet = Planet.query.get(planet_id)

    if not user or not planet:
        return jsonify({"msg": "Usuario o planeta no encontrado"}), 404

    if planet not in user.favorite_planets:
        return jsonify({"msg": "El planeta no está en favoritos"}), 400

    user.favorite_planets.remove(planet)
    db.session.commit()

    return jsonify({"msg": "Planeta eliminado de favoritos"}), 200

@favorites_bp.route('/favorite/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_favorite_vehicle(vehicle_id):
    user = User.query.get(g.user_id)
    vehicle = Vehicle.query.get(vehicle_id)

    if not user or not vehicle:
        return jsonify({"msg": "Usuario o vehículo no encontrado"}), 404

    if vehicle not in user.favorite_vehicles:
        return jsonify({"msg": "El vehículo no está en favoritos"}), 400

    user.favorite_vehicles.remove(vehicle)
    db.session.commit()

    return jsonify({"msg": "Vehículo eliminado de favoritos"}), 200