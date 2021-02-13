from django.db import models

# Create your models here.
class APIModel(models.Model):
    name=models.CharField(max_length=150,null=False)
    SN=models.CharField(max_length=30,null=False)
    Address=models.CharField(max_length=255,null=False)
    Profession=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
