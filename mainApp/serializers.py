from .models import Gallery
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class GallerySerializer(ModelSerializer):
	image = serializers.ImageField(write_only=True, required=False)
	image_url = serializers.SerializerMethodField()
	class Meta:
		model = Gallery
		fields = ['id','name','image_url','image']

		
	def get_image_url(self, obj):
		if obj.image:
			return obj.image.url
		return None


