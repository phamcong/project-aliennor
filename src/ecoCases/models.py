from django.db import models


class EcoCase(models.Model):
    ecocase_title = models.CharField(max_length=200)
    ecocase_description = models.TextField(max_length=300)
    ecocase_characters = models.TextField(max_length=5000)
    pub_date = models.DateTimeField('date published')
    img_url_list = models.CharField(max_length=None)

    def __str__(self):
        return self.ecocase_title


class ESM(models.Model):
    ecocase = models.ForeignKey(EcoCase, on_delete=models.CASCADE)
    esm_title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.esm_title
