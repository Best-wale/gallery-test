from rest_framework import generics
from .models import Gallery
from .serializers import GallerySerializer

class ImageListView(generics.ListCreateAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GallerySerializer




