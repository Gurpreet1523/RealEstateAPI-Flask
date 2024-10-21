from werkzeug.security import generate_password_hash
from repository.user_repository import UserRepository
from models.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class UserService:
    @staticmethod
    def create_user(name, email, password, phone_number, role):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, password=hashed_password, phone_number=phone_number, role=role)
        UserRepository.save_user(user)
        return user

    @staticmethod
    def get_user_by_email(email):
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return None
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.phone_number = data.get('phone_number', user.phone_number)

        return UserRepository.update_user(user_id, data)

    @staticmethod
    def authenticate_user(email, password):
        user = UserRepository.get_user_by_email(email=email)
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return False
        return UserRepository.delete_user(user_id)
