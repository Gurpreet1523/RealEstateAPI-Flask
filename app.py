import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger
from flask_cors import CORS

from controller.agentController import agent_bp
from controller.favouritesController import favourites_bp
from controller.inquiryController import inquiry_bp
from controller.openHouseController import openHouse_bp
from models.models import db
from flask_bcrypt import Bcrypt
from config import Config
from controller.userController import user_bp
from controller.propertyController import property_bp

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
#CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)

# Initialize database
db.init_app(app)

bcrypt = Bcrypt(app)
# Initialize JWT
jwt = JWTManager(app)
jwt.algorithms = {'HS256'}

# Initialize Swagger
swagger = Swagger(app)

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(property_bp)
app.register_blueprint(openHouse_bp)
app.register_blueprint(inquiry_bp)
app.register_blueprint(favourites_bp)
app.register_blueprint(agent_bp)


# Swagger UI configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # The path to your swagger.json file
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Real Estate API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
# Debugging route for testing
@app.route('/test')
def test():
    return "Hello World"

if __name__ == '__main__':
    #print("Swagger JSON Path:", os.path.join(app.root_path, 'static', 'swagger.json'))  # Print the swagger.json path for debugging
    app.run(debug=True)
