from repository.open_house_repository import OpenHouseRepository
from models.models import OpenHouse


class OpenHouseService:

    @staticmethod
    def create_open_house(data):
        open_house = OpenHouse(
            property_id=data['property_id'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            date=data['date']
        )
        OpenHouseRepository.create_open_house(open_house)
        return open_house

    @staticmethod
    def get_all_open_house():
        return OpenHouseRepository.get_all_open_house()

    @staticmethod
    def get_open_house(open_house_id):
        return OpenHouseRepository.get_open_house(open_house_id)

    @staticmethod
    def update_open_house(open_house_id, data):
        open_house = OpenHouseRepository.get_open_house(open_house_id)
        if open_house:
            open_house.start_time = data.get('start_time', open_house.start_time)
            open_house.end_time = data.get('end_time', open_house.end_time)
            open_house.date = data.get('date', open_house.date)
            OpenHouseRepository.update_open_house(open_house_id, data)
        return open_house

    @staticmethod
    def delete_open_house(open_house_id):
        open_house = OpenHouseRepository.get_open_house(open_house_id)
        if not open_house:
            return False
        return OpenHouseRepository.delete_open_house(open_house_id)
