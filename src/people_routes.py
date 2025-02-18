from flask import Blueprint, request, jsonify
from models import db, People
from datetime import datetime, timezone

people_bp = Blueprint('people_bp', __name__)

@people_bp.route('/people', methods=['GET'])
def handle_hello():
    response_body = {
        "msg": "Hello, this is your GET /people response "
    }
    return jsonify(response_body), 200

@people_bp.route('/people', methods=['POST'])
def add_people():
    body = request.get_json()  # obtener los datos del cuerpo de la solicitud

    if body is None:
        return jsonify({"msg": "El cuerpo de la solicitud está vacío"}), 400
    if 'name' not in body or 'birth_year' not in body:
        return jsonify({"msg": "Faltan campos obligatorios: name y/o birth_year"}), 400

    people = People(
        birth_year=body['birth_year'],
        created=body.get('created', datetime.now(timezone.utc)),
        edited=body.get('edited', datetime.now(timezone.utc)),
        eye_color=body.get('eye_color', ''),
        gender=body.get('gender', ''),
        hair_color=body.get('hair_color', ''),
        height=body.get('height', ''),
        homeworld=body.get('homeworld', ''),
        image=body.get('image', ''),
        mass=body.get('mass', ''),
        name=body['name'],
        skin_color=body.get('skin_color', ''),
        uid=body.get('uid', None),
        url=body.get('url', '')
    )

    db.session.add(people)
    db.session.commit()

    return jsonify({
        "msg": "Persona creada con éxito",
        "people": people.serialize()
    }), 201

@people_bp.route('/people/<int:people_id>', methods=['DELETE'])
def delete_people(people_id):
    people = People.query.get(people_id)
    if people is None:
        return jsonify({"msg": "Persona no encontrada"}), 404

    db.session.delete(people)
    db.session.commit()

    return jsonify({"msg": "Persona eliminada con éxito", "people_id": people_id}), 200

@people_bp.route('/peoples', methods=['GET'])
def get_all_peoples():
    peoples = People.query.all()
    peoples_list = [people.serialize() for people in peoples]
    
    return jsonify(peoples_list), 200

@people_bp.route('/reset_peoples', methods=['POST'])
def reset_peoples():
    try:
        # Eliminar todos los registros de la tabla People
        People.query.delete()
        db.session.commit()

        # Reiniciar el contador de id en PostgreSQL
        db.session.execute("ALTER SEQUENCE people_id_seq RESTART WITH 1")
        db.session.commit()

        return jsonify({"msg": "Todas las personas han sido eliminadas y el contador de ID ha sido reiniciado"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@people_bp.route('/people/<int:people_id>', methods=['GET'])
def get_people_by_id(people_id):
    people = People.query.get(people_id)
    if people is None:
        return jsonify({"msg": "Persona no encontrada"}), 404

    return jsonify(people.serialize()), 200