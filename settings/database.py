import motor
from decouple import config


DATABASE_URL = config('DATABASE_URL', 'mongodb://localhost:27017')
DATABASE_NAME = config('DATABASE_NAME', 'default')

database = motor.MotorClient(DATABASE_URL)[DATABASE_NAME]
