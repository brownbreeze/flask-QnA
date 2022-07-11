from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'G\xe2(\x97\xa1\x13K\x00\xc5\xad\x14\x8e\xfb4\xfb\x10'
