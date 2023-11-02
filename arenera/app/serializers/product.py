from rest_framework import serializers

from app.models .product import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state','create_date','modified_date','delete_date')

    def to_representation(self,instance):
        return {
            'id': instance.id,         
            'description': instance.description,
            'image': instance.image.url if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'price': instance.price,
        }

class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state','create_date','modified_date','delete_date') 
    