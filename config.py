import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'ou-will-never-guess'


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgres://sxpkcgcuxxjjxg:EDESil4B-dUZHxo-1Fif8pwkU9@ec2-54-83-56-177.compute-1.amazonaws.com:5432/da0if8ihlmlroa"
FILESTOREK = "AKIAJSFCV66627WSDHBQ"
FILESTOREKS = "xf2lCBd4jUa6ZvX1UX1FR4EXEDUQh9aDUkOmlVRP"
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['pdf'])


SQLALCHEMY_TRACK_MODIFICATIONS = True