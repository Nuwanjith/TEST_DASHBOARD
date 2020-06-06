from django.db import models

# Create your models here.
class Upload(models.Model):
    filename = models.CharField(max_length=200)
    test_type = models.CharField(max_length=300)
    created_time = models.DateTimeField()

