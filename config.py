from os import environ


# Google Cloud Storage
bucketName = environ.get('techhealthtools')
bucketFolder = environ.get('do_images')

# Data
localFolder = environ.get('/var/www/html/down_images')

