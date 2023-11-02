from rest_framework import serializers
from app.models.sale import Sale
from app.serializers.detail_sale_product import DetailSaleSerializer
from app.serializers.client import CLientSerializer
from app.serializers.user import UserSerializer

class SaleSerializer(serializers.ModelSerializer):
    details = DetailSaleSerializer(many=True, read_only=True)
    client = CLientSerializer(many=False,read_only=True)
    user = UserSerializer(many=False,read_only=True)
    
    class Meta:
        model = Sale
        fields = '__all__'