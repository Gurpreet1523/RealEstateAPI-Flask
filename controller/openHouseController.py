from flask import Blueprint, request, jsonify
from services.open_house_service import OpenHouseService
from flask_jwt_extended import jwt_required, get_jwt_identity

openHouse_bp = Blueprint('openHouse_bp', __name__)


@openHouse_bp.route('/open_houses', methods=['POST'])
@jwt_required()
def create_new_open_house():
    data = request.get_json()
    open_house = OpenHouseService.create_open_house(data)
    return jsonify({"open_house_id": open_house.open_house_id, "property_id": open_house.property_id}), 201


@openHouse_bp.route('/open_houses', methods=['GET'])
def get_all_open_house():
    open_houses = OpenHouseService.get_all_open_house()
    return jsonify([open_house.to_dict() for open_house in open_houses]), 200


@openHouse_bp.route('/open_houses/<int:open_house_id>', methods=['GET'])
def get_open_house_details(open_house_id):
    open_house = OpenHouseService.get_open_house(open_house_id)
    if not open_house:
        return jsonify({"message": "Open house not found"}), 404
    return jsonify({"open_house_id": open_house.open_house_id, "property_id": open_house.property_id,
                    "date": open_house.date}), 200


@openHouse_bp.route('/open_houses/<int:open_house_id>', methods=['PUT'])
@jwt_required()
def update_open_house_details(open_house_id):
    data = request.get_json()
    open_house = OpenHouseService.update_open_house(open_house_id, data)
    if not open_house:
        return jsonify({"message": "Open house not found"}), 404
    return jsonify({"message": "Open house updated successfully"}), 200


@openHouse_bp.route('/open_houses/<int:open_house_id>', methods=['DELETE'])
@jwt_required()
def delete_open_house_details(open_house_id):
    open_house = OpenHouseService.delete_open_house(open_house_id)
    if not open_house:
        return jsonify({"message": "Open house not found"}), 404
    return jsonify({"message": "Open house deleted successfully"}), 200
