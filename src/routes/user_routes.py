from flask import Blueprint, request, jsonify
from models import db, User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=['GET'])
def handle_hello():
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return jsonify(response_body), 200

@user_bp.route('/user', methods=['POST'])
def add_user():
    body = request.get_json()  # obtener los datos del cuerpo de la solicitud

    if body is None:
        return jsonify({"msg": "El cuerpo de la solicitud está vacío"}), 400
    if 'email' not in body or 'password' not in body:
        return jsonify({"msg": "Faltan campos obligatorios: email y/o password"}), 400

    email = body['email']
    password = body['password']
    is_active = body.get('is_active', True)  # Valor por defecto True si no se proporciona

    # Crear un nuevo usuario
    new_user = User(email=email, password=password, is_active=is_active)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "msg": "Usuario creado con éxito",
        "user": {
            "email": new_user.email,
            "is_active": new_user.is_active
        }
    }), 201

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": "Usuario eliminado con éxito", "user_id": user_id}), 200

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [{"id": user.id, "email": user.email, "is_active": user.is_active} for user in users]
    
    return jsonify(users_list), 200

@user_bp.route('/reset_users', methods=['POST'])
def reset_users():
    try:
        # Eliminar todos los registros de la tabla User
        User.query.delete()
        db.session.commit()

        # Reiniciar el contador de id en PostgreSQL
        db.session.execute("ALTER SEQUENCE user_id_seq RESTART WITH 1")
        db.session.commit()

        return jsonify({"msg": "Todos los usuarios han sido eliminados y el contador de ID ha sido reiniciado"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    user_data = {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active
    }

    return jsonify(user_data), 200