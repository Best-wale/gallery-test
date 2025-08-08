from .models import Gallery
from rest_framework.serializers import ModelSerializer

class GallerySerializer(ModelSerializer):
	class Meta:
		model = Gallery
		fields = '__all__'

