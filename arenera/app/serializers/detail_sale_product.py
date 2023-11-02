from rest_framework import serializers
from app.models.detail_sale_product import DetailSale


class DetailSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSale
        fields = '__all__'