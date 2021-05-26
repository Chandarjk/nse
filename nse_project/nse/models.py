from django.db import models

# Create your models here.
class NseSettings(models.Model):
    client = models.CharField(max_length=100,default=None)
    nse_list = models.CharField(max_length=100,default=None)
    path = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=50)

    def __str__(self):
        return self.client

class NseReport(models.Model):
    nse = models.ForeignKey(NseSettings, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=100)
    generate_date = models.DateTimeField(default=None)

    def __str__(self):
        return self.file_path
