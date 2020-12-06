import motor
from decouple import config


DATABASE_URL = config('DATABASE_URL', 'mongodb://mongodb0.example.com:27017/default')
database = motor.MotorClient(DATABASE_URL)

DATABASE_NAME = database
