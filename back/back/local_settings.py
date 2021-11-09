import os

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('DB_NAME', 'db_test'),
        'ENFORCE_SCHEMA': False,
        'TEST': {
            'NAME': 'test_mytestdb'
        },
        'CLIENT': {
            'host': os.environ.get('DB_HOST', 'db'),
            'port': 27017,
            'username': os.environ.get('DB_USERNAME', 'root'),
            'password': os.environ.get('DB_PASSWD', 'thepassis1')
        }
    }
}