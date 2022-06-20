# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--19@^te@be81h&3l5nj-a$9bwksk-kp1r#7##c%ac=)x6ah%g#'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'ARCHeesecake$$08'
    }
}