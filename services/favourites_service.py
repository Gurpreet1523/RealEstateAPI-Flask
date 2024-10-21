from repository.favourites_repository import FavouritesRepository
from models.models import Favorite


class FavouritesService:

    @staticmethod
    def add_favorite(user_id, property_id):
        favorite = Favorite(user_id=user_id, property_id=property_id)
        FavouritesRepository.add_favorite(favorite)
        return favorite

    @staticmethod
    def get_favorites_for_user(user_id):
        return FavouritesRepository.get_favorites_for_user(user_id=user_id)

    @staticmethod
    def delete_favorite(favorite_id):
        favorite = Favorite.query.get(favorite_id)
        if favorite:
            FavouritesRepository.delete_favorite(favorite_id)
        return favorite
