from django.db import models
from cloudinary.models import CloudinaryField
class Gallery(models.Model):
	name = models.CharField(max_length=100)
	#image = models.ImageField(upload_to='gallery')
	image = CloudinaryField('Image', blank=True, resource_type='auto')
	date_created = models.DateTimeField(auto_now=True)