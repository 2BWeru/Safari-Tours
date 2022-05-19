import os
# parent Config class contains configurations that are used in both production and development stages.
class Config:
    SECRET_KEY = 'Black'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tours:2022@localhost/safari'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # mail
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 465
    # update it with your gmail
    MAIL_USERNAME = 'your_mail@gmail.com'
    # update it with your password
    MAIL_PASSWORD= 'your_email_password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


# ProdConfig subclass contains configurations that are used in production stages of our application and inherits from the parent Config class.
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


# DevConfig subclass contains configurations that are used in development stages of our application and inherits from the parent Config class.
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

