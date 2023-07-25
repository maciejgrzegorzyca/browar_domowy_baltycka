from django.db import models

# Create your models here.
class Batch(models.Model):
    namebatch = models.CharField(max_length=26, null=False)
    stylebatch = models.CharField(max_length=26, null=False)
    ogbatch = models.FloatField(max_length=4, null=False)
    abvbatch = models.FloatField(max_length=4, null=False)
    ibubatch = models.FloatField(max_length=4, null=False)