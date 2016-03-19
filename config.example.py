import os

WTF_CSRF_ENABLED = True
SECRET_KEY = '#TODO'


basedir = os.path.abspath(os.path.dirname(__file__))

#testing
#SQLALCHEMY_DATABASE_URI = "postgres://user@localhost/database"

#production
SQLALCHEMY_DATABASE_URI = "postgres://user:password@server:port/database"

#amazon s3
FILESTOREK = "#TODO"
FILESTOREKS = "#TODO"

#very first testing
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['pdf'])


SQLALCHEMY_TRACK_MODIFICATIONS = True