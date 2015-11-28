# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES  =  {
    'default':  {
    'ENGINE':  'django.db.backends.mysql',
    'HOST':  'localhost',
    'USER':  'root',
    'PASSWORD':  'root',
    'NAME':  'students_db',
    }
}

#mysql.connector.django
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
#    }
#}
