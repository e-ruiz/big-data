# -*- coding: utf-8 -*-

# Define the application directory
import os


# Statement for enabling the development environment
DEBUG = True if os.environ['FLASK_ENV'] == 'development' else False

# Flask-Debugtoolbar
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False

BASE_DIR = os.path.abspath(os.path.dirname(__file__) + os.path.join('/../'))

# Exemplo Cassandra DB
CASSANDRA_HOST = os.environ.get('FLASK_CASS_HOST')
CASSANDRA_PORT = os.environ.get('FLASK_CASS_PORT')
CASSANDRA_USER = os.environ.get('FLASK_CASS_USER')
CASSANDRA_PASS = os.environ.get('FLASK_CASS_PASS')

# Exemplo MongoDB
# MONGO_USR = os.environ.get('FLASK_MONGO_USR') # eric_O132Dhp1I9m2
# MONGO_PWD = os.environ.get('FLASK_MONGO_PWD') # kvbZcqSi4XB58D72
# MONGO_URI = 'mongodb://%s:%s@cluster0-shard-00-00-hgixp.mongodb.net:27017,cluster0-shard-00-01-hgixp.mongodb.net:27017,cluster0-shard-00-02-hgixp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority' \
#         % (MONGO_USR, MONGO_PWD) 

# Exemplo SQLite
# DATABASE_NAME = 'storage.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DATABASE_NAME)
# DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# Secret key for signing cookies
SECRET_KEY = """This is the $ekkret:
é1fxMuHuPzFsHÜfs5kuBh2lHTutPcwKafXN.bK0ZRNPnEbxYDl1L6m7heNFUDAI1
"""

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = """The secret is:
6*F0wPBR_Ae0o,wr0DF7xB1StYL6VMgDtFRUCqlh4S3ApiªTRS8XM4fgujyu8UT6
"""