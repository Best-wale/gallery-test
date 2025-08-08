from django.db import models

class Gallery(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='gallery')
	date_created = models.DateTimeField(auto_now=True)