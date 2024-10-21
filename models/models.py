import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15))
    role = db.Column(db.String(10), nullable=False)

    # Define reverse relationship with Agent
    agents = relationship('Agent', back_populates='user', cascade="all, delete-orphan")

    property = relationship('Property', back_populates='user', cascade="all, delete-orphan")

    def set_password(self, password):
        """Hashes and sets the password."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Checks the password against the stored hash."""
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        """Convert user to dictionary (optional but useful)."""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'role': self.role
        }


class Property(db.Model):
    __tablename__ = 'Properties'

    property_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    province = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=True)
    bathrooms = db.Column(db.Integer, nullable=True)
    square_feet = db.Column(db.Integer, nullable=True)
    listing_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)
    images = db.Column(db.Text, nullable=True)

    user = db.relationship('User', backref='properties')

    # Define a to_dict method
    def to_dict(self):
        return {
            'property_id': self.property_id,
            'user_id': self.user_id,
            'address': self.address,
            'city': self.city,
            'province': self.province,
            'postal_code': self.postal_code,
            'price': str(self.price),  # convert Decimal to string to avoid issues with JSON serialization
            'property_type': self.property_type,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'square_feet': self.square_feet,
            'listing_date': self.listing_date.isoformat(),  # convert date to string format
            'status': self.status,
            'description': self.description,
            'images': self.images
        }


class Agent(db.Model):
    __tablename__ = 'Agents'
    agent_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    agency_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String(255))

    user = db.relationship('User', backref='agent')

    def to_dict(self):
        """Convert  to dictionary (optional but useful)."""
        return {
            'agent_id' : self.agent_id,
            'user_id': self.user_id,
            'agency_name': self.agency_name,
            'phone_number': self.phone_number,
            'email': self.email,
        }

class OpenHouse(db.Model):
    __tablename__ = 'Open_Houses'
    open_house_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_id = db.Column(db.Integer, db.ForeignKey('Properties.property_id'), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    date = db.Column(db.Date)

    property = db.relationship('Property', backref='open_houses')

    def to_dict(self):
        """Convert  to dictionary (optional but useful)."""
        return {
            'open_house_id': self.open_house_id,
            'property_id': self.property_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'date': self.date,
        }

class Favorite(db.Model):
    __tablename__ = 'Favorites'
    favorite_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('Properties.property_id'), nullable=False)

    user = db.relationship('User', backref='favorites')
    property = db.relationship('Property', backref='favorites')

    def to_dict(self):
        """Convert  to dictionary (optional but useful)."""
        return {
            'favorite_id': self.favorite_id,
            'user_id': self.user_id,
            'property_id': self.property_id,

        }

class Inquiry(db.Model):
    __tablename__ = 'Inquiries'
    inquiry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_id = db.Column(db.Integer, db.ForeignKey('Properties.property_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    inquiry_date = db.Column(db.DateTime, default=datetime.timezone.utc)

    property = db.relationship('Property', backref='inquiries')
    user = db.relationship('User', backref='inquiries')

    def to_dict(self):
        """Convert  to dictionary (optional but useful)."""
        return {
            'inquiry_id': self.inquiry_id,
            'property_id': self.property_id,
            'user_id': self.user_id,
            'message': self.message,
            'inquiry_date': self.inquiry_date,
        }