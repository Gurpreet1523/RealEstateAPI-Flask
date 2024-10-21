from models.models import Property, db


class PropertyRepository:
    @staticmethod
    def get_all_properties():
        return Property.query.all()

    @staticmethod
    def save_property(property):
        db.session.add(property)
        db.session.commit()

    def get_property_by_id(property_id):
        return Property.query.filter_by(property_id=property_id).first()

    @staticmethod
    def update_property(property_id, updated_data):
        property = Property.query.filter_by(property_id=property_id).first()
        if property:
            for key, value in updated_data.items():
                setattr(property, key, value)
            db.session.commit()
        return property

    @staticmethod
    def delete_property(property_id):
        property = Property.query.filter_by(property_id=property_id).first()
        if property:
            db.session.delete(property)
            db.session.commit()
            return True
        return False
