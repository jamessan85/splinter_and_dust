from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_3LMtAyn1SOaq9o62EREYrSDe')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_FtpgmAnp9OLHr33GwaGtkgAV')
