from flask import Blueprint, request, jsonify
from models import db, Planet

planet_bp = Blueprint('planet_bp', __name__)

@planet_bp.route('/planet', methods=['GET'])
def handle_hello():
    response_body = {
        "msg": "Hello, this is your GET /planet response "
    }
    return jsonify(response_body), 200

@planet_bp.route('/planet', methods=['POST'])
def add_planet():
    body = request.get_json()  # obtener los datos del cuerpo de la solicitud

    if body is None:
        return jsonify({"msg": "El cuerpo de la solicitud está vacío"}), 400
    if 'name' not in body or 'climate' not in body:
        return jsonify({"msg": "Faltan campos obligatorios: name y/o climate"}), 400

    planet = Planet(
        climate=body['climate'],
        created=body.get('created', datetime.now(timezone.utc)),
        diameter=body.get('diameter', ''),
        edited=body.get('edited', datetime.now(timezone.utc)),
        gravity=body.get('gravity', ''),
        image=body.get('image', ''),
        name=body['name'],
        orbital_period=body.get('orbital_period', ''),
        population=body.get('population', ''),
        rotation_period=body.get('rotation_period', ''),
        surface_water=body.get('surface_water', ''),
        terrain=body.get('terrain', ''),
        uid=body.get('uid', None),
        url=body.get('url', '')
    )

    db.session.add(planet)
    db.session.commit()

    return jsonify({
        "msg": "Planeta creado con éxito",
        "planet": planet.serialize()
    }), 201

@planet_bp.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg": "Planeta no encontrado"}), 404

    db.session.delete(planet)
    db.session.commit()

    return jsonify({"msg": "Planeta eliminado con éxito", "planet_id": planet_id}), 200

@planet_bp.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    planets_list = [planet.serialize() for planet in planets]
    
    return jsonify(planets_list), 200

@planet_bp.route('/reset_planets', methods=['POST'])
def reset_planets():
    try:
        # Eliminar todos los registros de la tabla Planet
        Planet.query.delete()
        db.session.commit()

        # Reiniciar el contador de id en PostgreSQL
        db.session.execute("ALTER SEQUENCE planet_id_seq RESTART WITH 1")
        db.session.commit()

        return jsonify({"msg": "Todos los planetas han sido eliminados y el contador de ID ha sido reiniciado"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@planet_bp.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg": "Planeta no encontrado"}), 404

    return jsonify(planet.serialize()), 200