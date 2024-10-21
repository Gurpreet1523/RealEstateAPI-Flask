from models.models import Favorite, db


class FavouritesRepository:

    @staticmethod
    def add_favorite(favourite):
        db.session.add(favourite)
        db.session.commit()

    @staticmethod
    def get_favorites_for_user(user_id):
        return Favorite.query.filter_by(user_id=user_id).all()

    @staticmethod
    def delete_favorite(favorite_id):
        favorite = Favorite.query.get(favorite_id)
        if favorite:
            db.session.delete(favorite)
            db.session.commit()
        return favorite
