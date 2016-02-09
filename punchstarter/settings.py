import os
import cloudinary

# DEBUG=True
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", 'sqlite:///' + BASE_DIR + '/app.db')

DEBUG=os.environ.get('DEBUG', True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", 'sqlite:///' + BASE_DIR + '/app.db')

# setup your cloudnary api details here

cloudinary.config(
  cloud_name = CLOUDINARY_CLOUD_NAME,
  api_key = CLOUDINARY_API_KEY,
  api_secret = CLOUDINARY_API_SECRET
)
