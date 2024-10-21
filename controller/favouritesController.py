from flask import Blueprint, request, jsonify
from services.favourites_service import FavouritesService
from flask_jwt_extended import jwt_required, get_jwt_identity

favourites_bp = Blueprint('favourites_bp', __name__)


@favourites_bp.route('/favorites', methods=['POST'])
@jwt_required()
def add_to_favorites():
    current_user = get_jwt_identity()
    data = request.get_json()
    favorite = FavouritesService.add_favorite(current_user, data['property_id'])
    return jsonify({"favorite_id": favorite.favorite_id, "property_id": favorite.property_id}), 201


@favourites_bp.route('/favorites', methods=['GET'])
@jwt_required()
def get_user_favorites():
    current_user = get_jwt_identity()
    favorites = FavouritesService.get_favorites_for_user(current_user)
    favorites_list = [{'favorite_id': f.favorite_id, 'property_id': f.property_id} for f in favorites]
    return jsonify(favorites_list), 200


@favourites_bp.route('/favorites/<int:favorite_id>', methods=['DELETE'])
@jwt_required()
def remove_from_favorites(favorite_id):
    favorite = FavouritesService.delete_favorite(favorite_id)
    if not favorite:
        return jsonify({"message": "Favorite not found"}), 404
    return jsonify({"message": "Favorite deleted successfully"}), 200
