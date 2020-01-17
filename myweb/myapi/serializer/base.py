from rest_framework import serializers

from myapi.model.base import Image


class ImageSerializer(serializers.ModelSerializer):
    """Image Serializer"""
    class Meta:
        model = Image
        exclude = ('created', 'updated',)
