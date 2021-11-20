from django.db import models


# Create your models here.

class UrlRedirect(models.Model):
    destiny = models.URLField(max_length=512)
    slug = models.SlugField(max_length=120, unique=True)
    created_in = models.DateTimeField(auto_now_add=True)
    update_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UrlRedirect para {self.destiny}'


class UrlLog(models.Model):
    created_in = models.DateTimeField(auto_now_add=True)
    origin = models.URLField(max_length=512, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(UrlRedirect, models.DO_NOTHING, related_name='logs')
