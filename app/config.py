import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fitness.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
