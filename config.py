import os

MONGODB_SETTINGS = {
    'DB': 'blindly'
}

SECRET_KEY = os.environ.get('MONGO_BLINDLY_SECRET_KEY')
