import os
import urllib.parse as up
import psycopg2

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    '''
        Set config variables for the flask app
        Using Environment variables where available.
        Otherwise create the config variable if not done already
    '''


    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Maybe I will try to make CSS this time'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICAITONS = False
    up.uses_netloc.append("postgres")
    url = up.urlparse(os.environ["DATABASE_URI"])
    conn = psycopg2.connect("dbname='mdclizft' user='mdclizft' password='PLGuWSNox1Y4m2pK0HExSmOq5F9ytb60' host='kashin.db.elephantsql.com' port='5432'")