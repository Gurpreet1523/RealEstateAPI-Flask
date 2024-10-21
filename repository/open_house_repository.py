from models.models import OpenHouse, db


class OpenHouseRepository:

    @staticmethod
    def get_all_open_house():
        return OpenHouse.query.all()

    @staticmethod
    def create_open_house(open_house):
        db.session.add(open_house)
        db.session.commit()


    @staticmethod
    def get_open_house(open_house_id):
        return OpenHouse.query.filter_by(open_house_id=open_house_id).first()

    @staticmethod
    def update_open_house(open_house_id, data):
        open_house = OpenHouse.query.filter_by(open_house_id=open_house_id).first()
        if open_house:
            for key, value in data.items():
                setattr(open_house, key, value)
            db.session.commit()
        return open_house

    @staticmethod
    def delete_open_house(open_house_id):
        open_house = OpenHouse.query.filter_by(open_house_id=open_house_id).first()
        if open_house:
            db.session.delete(open_house)
            db.session.commit()
            return True
        return open_house
