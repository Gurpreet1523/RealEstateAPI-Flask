from repository.property_repository import PropertyRepository
from models.models import Property


class PropertyService:
    @staticmethod
    def add_property(user_id, address, city, province, postal_code, price, property_type, bedrooms, bathrooms,
                     square_feet, listing_date, status, description, images):
        property = Property(
            user_id=user_id, address=address, city=city, province=province, postal_code=postal_code,
            price=price, property_type=property_type, bedrooms=bedrooms, bathrooms=bathrooms,
            square_feet=square_feet, listing_date=listing_date, status=status, description=description,
            images=images
        )
        PropertyRepository.save_property(property)
        return property

    @staticmethod
    def get_all_properties():
        return PropertyRepository.get_all_properties()

    @staticmethod
    def get_property_by_id(property_id):
        return PropertyRepository.get_property_by_id(property_id)

    @staticmethod
    def update_property(property_id, data):
        property = PropertyRepository.get_property_by_id(property_id)
        if not property:
            return None
        property.address = data.get('address', property.address)
        property.city = data.get('city', property.city)
        property.province = data.get('province', property.province)
        property.postal_code = data.get('postal_code', property.postal_code)
        property.price = data.get('price', property.price)
        property.property_type = data.get('property_type', property.property_type)
        property.bedrooms = data.get('bedrooms', property.bedrooms)
        property.bathrooms = data.get('bathrooms', property.bathrooms)
        property.square_feet = data.get('square_feet', property.square_feet)
        property.listing_date = data.get('listing_date', property.listing_date)
        property.status = data.get('status', property.status)
        property.description = data.get('description', property.description)
        property.images = data.get('images', property.images)

        return PropertyRepository.update_property(property_id, data)

    @staticmethod
    def delete_property(property_id):
        property = PropertyRepository.get_property_by_id(property_id)
        if not property:
            return False
        return PropertyRepository.delete_property(property_id)
