import os
from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://@localhost\\SQLEXPRESS/realEstateDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.urandom(24)
    #print(JWT_SECRET_KEY) # Randomly generated secret key
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


