from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('mysql://b91e600fa9d9e1:b19256f2@eu-cdbr-west-01.cleardb.com/heroku_311bf5ff6bb89d3?')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_3LMtAyn1SOaq9o62EREYrSDe')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_FtpgmAnp9OLHr33GwaGtkgAV')
