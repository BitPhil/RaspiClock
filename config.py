import secrets

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = secrets.token_urlsafe(16)

    #DB_NAME
    #DB_USERNAME
    #DB_PASSWORD

    #UPLOAD = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class Production(Config):
    pass

class Develop(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db" 

class Testing(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False


    