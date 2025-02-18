from flask import Blueprint, request, jsonify
from models import db, Vehicle
from datetime import datetime, timezone

vehicle_bp = Blueprint('vehicle_bp', __name__)

@vehicle_bp.route('/vehicle', methods=['GET'])
def handle_hello():
    response_body = {
        "msg": "Hello, this is your GET /vehicle response "
    }
    return jsonify(response_body), 200

@vehicle_bp.route('/vehicle', methods=['POST'])
def add_vehicle():
    body = request.get_json()  # obtener los datos del cuerpo de la solicitud

    if body is None:
        return jsonify({"msg": "El cuerpo de la solicitud está vacío"}), 400
    if 'name' not in body or 'model' not in body:
        return jsonify({"msg": "Faltan campos obligatorios: name y/o model"}), 400

    vehicle = Vehicle(
        cargo_capacity=body['cargo_capacity'],
        consumables=body['consumables'],
        cost_in_credits=body['cost_in_credits'],
        created=body.get('created', datetime.now(timezone.utc)),
        crew=body['crew'],
        edited=body.get('edited', datetime.now(timezone.utc)),
        films=body.get('films', []),
        image=body['image'],
        length=body['length'],
        manufacturer=body['manufacturer'],
        max_atmosphering_speed=body['max_atmosphering_speed'],
        model=body['model'],
        name=body['name'],
        passengers=body['passengers'],
        pilots=body.get('pilots', []),
        uid=body.get('uid', None),
        url=body.get('url', ''),
        vehicle_class=body['vehicle_class']
    )

    db.session.add(vehicle)
    db.session.commit()

    return jsonify({
        "msg": "Vehículo creado con éxito",
        "vehicle": vehicle.serialize()
    }), 201

@vehicle_bp.route('/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({"msg": "Vehículo no encontrado"}), 404

    db.session.delete(vehicle)
    db.session.commit()

    return jsonify({"msg": "Vehículo eliminado con éxito", "vehicle_id": vehicle_id}), 200

@vehicle_bp.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    vehicles_list = [vehicle.serialize() for vehicle in vehicles]
    
    return jsonify(vehicles_list), 200

@vehicle_bp.route('/reset_vehicles', methods=['POST'])
def reset_vehicles():
    try:
        # Eliminar todos los registros de la tabla Vehicle
        Vehicle.query.delete()
        db.session.commit()

        # Reiniciar el contador de id en PostgreSQL
        db.session.execute("ALTER SEQUENCE vehicle_id_seq RESTART WITH 1")
        db.session.commit()

        return jsonify({"msg": "Todos los vehículos han sido eliminados y el contador de ID ha sido reiniciado"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@vehicle_bp.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle_by_id(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({"msg": "Vehículo no encontrado"}), 404

    return jsonify(vehicle.serialize()), 200