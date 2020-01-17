from rest_framework import generics
from myapi.model.base import Image
from myapi.serializer.base import ImageSerializer


class ImageList(generics.ListCreateAPIView):
    """ image list / create """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """ image retrieve / update / delete """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
