from config.default import *
from logging.config import dictConfig


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'G\xe2(\x97\xa1\x13K\x00\xc5\xad\x14\x8e\xfb4\xfb\x10'

dictConfig({
    'version':1,
    'formatters':{
        'default':{
            'format':'[%(asctime)s%] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers':{
        'file':{
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes':1024*1024*5, # 5 MB
            'backupCount':5,
            'formatter':'default',
        },
    },
    'root':{
        'level':'INFO',
        'handlers':['file']
    }
})
