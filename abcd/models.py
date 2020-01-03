from django.db import models

# Create your models here.
class Webd(models.Model):
	name = models.CharField(max_length=320)