from flask import Blueprint, request, jsonify
from services.inquiry_service import InquiryService
from flask_jwt_extended import jwt_required, get_jwt_identity

inquiry_bp = Blueprint('inquiry_bp', __name__)


@inquiry_bp.route('/inquiries', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    user_id = get_jwt_identity()
    property_id = data['property_id']
    message = data['message']
    inquiry_date = data['inquiry_date']
    inquiry = InquiryService.create_inquiry(user_id, property_id, message, inquiry_date)
    return jsonify({"inquiry_id": inquiry.inquiry_id, "message": "Inquiry created"}), 201


@inquiry_bp.route('/inquiries', methods=['GET'])
@jwt_required()
def get_all():
    inquiries = InquiryService.get_all_inquiries()
    return jsonify([{
        "inquiry_id": inquiry.inquiry_id,
        "user_id": inquiry.user_id,
        "property_id": inquiry.property_id,
        "message": inquiry.message,
        "inquiry_date": inquiry.inquiry_date
    } for inquiry in inquiries]), 200


@inquiry_bp.route('/inquiries/<int:inquiry_id>', methods=['GET'])
@jwt_required()
def get_one(inquiry_id):
    inquiry = InquiryService.get_inquiry_by_id(inquiry_id)
    if inquiry:
        return jsonify({
            "inquiry_id": inquiry.inquiry_id,
            "user_id": inquiry.user_id,
            "property_id": inquiry.property_id,
            "message": inquiry.message,
            "inquiry_date": inquiry.inquiry_date
        }), 200
    return jsonify({"message": "Inquiry not found"}), 404


@inquiry_bp.route('/inquiries/<int:inquiry_id>', methods=['PUT'])
@jwt_required()
def update(inquiry_id):
    data = request.get_json()
    inquiry = InquiryService.update_inquiry(inquiry_id, data['message'])
    if inquiry:
        return jsonify({"inquiry_id": inquiry.inquiry_id, "message": inquiry.message}), 200
    return jsonify({"message": "Inquiry not found"}), 404


@inquiry_bp.route('/inquiries/<int:inquiry_id>', methods=['DELETE'])
@jwt_required()
def delete(inquiry_id):
    inquiry = InquiryService.delete_inquiry(inquiry_id)
    if inquiry:
        return jsonify({"message": "Inquiry deleted"}), 200
    return jsonify({"message": "Inquiry not found"}), 404
