import datetime
from django.db import models
from django.utils import timezone
from django.forms import TextInput, Textarea
from django.core.files.storage import FileSystemStorage
from tinymce import models as tinymce_models


ecocase_image_fs = FileSystemStorage(location='/media/ecocases/')
esm_choices = (
    ('esm1', 'ESM1'),
    ('esm2', 'ESM2'),
    ('esm3', 'ESM3'),
    ('esm4', 'ESM4'),
    ('esm5', 'ESM5'),
    ('esm6', 'ESM6'),
    ('esm7', 'ESM7'),
    ('esm8', 'ESM8'),
)

def make_upload_path(instance, filename):
    file_root, file_ext = os.path.splitext(filename)
    dir 

class EcoCase(models.Model):
    ecocase_title = models.CharField(max_length=200)
    ecocase_description = tinymce_models.HTMLField()
    ecocase_characters = tinymce_models.HTMLField()
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
    esm_type = models.CharField(
        max_length=100, choices=esm_choices, default='ESM01')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.esm_title
