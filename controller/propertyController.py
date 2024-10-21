from flask import Blueprint, request, jsonify
from services.property_service import PropertyService
from flask_jwt_extended import jwt_required

property_bp = Blueprint('property_bp', __name__)


@property_bp.route('/properties', methods=['POST'])
#@jwt_required()
def add_property():
    data = request.get_json()
    property = PropertyService.add_property(
        user_id=data['user_id'], address=data['address'], city=data['city'],
        province=data['province'], postal_code=data['postal_code'], price=data['price'],
        property_type=data['property_type'], bedrooms=data.get('bedrooms'),
        bathrooms=data.get('bathrooms'), square_feet=data.get('square_feet'),
        listing_date=data['listing_date'], status=data['status'],
        description=data.get('description'), images=data.get('images')
    )
    return jsonify({"property_id": property.property_id}), 201


@property_bp.route('/properties', methods=['GET'])
def get_properties():
    properties = PropertyService.get_all_properties()
    return jsonify([prop.to_dict() for prop in properties])


@property_bp.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = PropertyService.get_property_by_id(property_id)
    if property:
        return jsonify(property.to_dict()), 200
    return jsonify({"msg": "Property not found"}), 404


@property_bp.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    data = request.get_json()
    property = PropertyService.update_property(property_id, data)
    if property:
        return jsonify({"property_id": property.property_id, "address": property.address}), 200
    return jsonify({"msg": "Property not found"}), 404


@property_bp.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    success = PropertyService.delete_property(property_id)
    if success:
        return jsonify({"msg": "Property deleted successfully"}), 200
    return jsonify({"msg": "Property not found"}), 404
