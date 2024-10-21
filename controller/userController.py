from flask import Blueprint, request, jsonify
from services.user_service import UserService
from flask_jwt_extended import create_access_token

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = UserService.create_user(data['name'], data['email'], data['password'], data['phone_number'],
                                   data['role'])
    user.set_password(data['password'])
    return jsonify({"user_id": user.user_id, "email": user.email}), 201


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = UserService.get_user_by_email(data['email'])
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.user_id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401


@user_bp.route('/logout', methods=['POST'])
def logout():
    # JWT does not handle server-side logout. You can use token blacklisting if necessary.
    return jsonify({"message": "User logged out successfully"}), 200
