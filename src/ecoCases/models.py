import datetime
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from tinymce.models import HTMLField

ecocase_image_fs = FileSystemStorage(location='/media/ecocases/')

class EcoCase(models.Model):
    ecocase_title = models.CharField(max_length=200)
    ecocase_description = models.TextField(max_length=300)
    ecocase_characters = HTMLField()
    timestamp = models.DateTimeField(null=True)
    ecocase_image_urls = models.CharField(max_length=2000, default='')
    ecocase_images = models.FileField(upload_to='ecocases', null=True)

    def __str__(self):
        return self.ecocase_title

    def ecocase_image_url_list(self):
        return self.ecocase_image_urls.split(';')

    def first_image_url(self):
        return self.ecocase_image_urls.split(';')[0]


class ESM(models.Model):
    ecocase = models.ForeignKey(EcoCase, on_delete=models.CASCADE)
    esm_title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.esm_title
