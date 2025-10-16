'''import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL = os.getenv('POSTGRES_URL')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PW = os.getenv('POSTGRES_PW')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = os.getenv('SECRET_KEY', 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm')
    SERVICE_BUS_CONNECTION_STRING = os.getenv('SERVICE_BUS_CONNECTION_STRING')
    SERVICE_BUS_QUEUE_NAME = os.getenv('SERVICE_BUS_QUEUE_NAME')
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

    '''
import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL = os.getenv('POSTGRES_URL','techconf-db-server.postgres.database.azure.com')
    POSTGRES_USER = os.getenv('POSTGRES_USER','Udacity_user@techconf-db-server')
    POSTGRES_PW = os.getenv('POSTGRES_PW','SQLp@12345') 
    POSTGRES_DB = os.getenv('POSTGRES_DB','techconfdb')
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = os.getenv('SECRET_KEY', 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm')
    SERVICE_BUS_CONNECTION_STRING = os.getenv('SERVICE_BUS_CONNECTION_STRING','Endpoint=sb://techconf-servicebus-udacity.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=MiQ5hXeLDSNTEBD7DIqtF4kVW+Ao5VYCX+ASbOvWH4g=')
    SERVICE_BUS_QUEUE_NAME = os.getenv('SERVICE_BUS_QUEUE_NAME','notificationqueue')
    ADMIN_EMAIL_ADDRESS= 'samret149@gmail.com'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
