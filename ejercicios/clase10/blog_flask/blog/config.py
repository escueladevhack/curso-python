# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI  = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = True

print("Loading configuration")