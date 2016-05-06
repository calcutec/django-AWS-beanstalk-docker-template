# custom_storages.py
# taken from:
# https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
# Fri Mar 11 16:36:50 EST 2016

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

#    def __init__(self, *args, **kwargs):
#        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
#        super(StaticStorage, self).__init__(*args, **kwargs)

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION

#    def __init__(self, *args, **kwargs):
#        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
#        super(StaticStorage, self).__init__(*args, **kwargs)
