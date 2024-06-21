from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        # Convert the Elasticsearch document to a dictionary
        return {
            'name': instance.name,
            'category': instance.category,
            'description': instance.description,
        }