from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_3LMtAyn1SOaq9o62EREYrSDe')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_FtpgmAnp9OLHr33GwaGtkgAV')
