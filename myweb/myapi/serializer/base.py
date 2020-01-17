from rest_framework import serializers

from myapi.model.commodity import Category


class ImageSerializer(serializers.ModelSerializer):
    """Image Serializer"""
    class Meta:
        model = Category
        exclude = ('created', 'updated',)