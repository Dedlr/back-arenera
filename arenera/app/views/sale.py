from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from app.models.sale import Sale
from app.models.detail_sale_product import DetailSale
from app.serializers.sale import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(state=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def retrieve(self, request, pk=None):
        try:
            sale = Sale.objects.get(pk=pk)  # Buscar la venta por ID
        except Sale.DoesNotExist:
            return Response({'error': 'Venta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(sale)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message': 'Venta registrada correctamente!'}, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            sale = Sale.objects.get(pk=pk)  # Buscar la venta por ID
        except Sale.DoesNotExist:
            return Response({'error': 'Venta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(sale, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Venta actualizada correctamente'}, status=status.HTTP_200_OK)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        sale = self.get_queryset().filter(id=pk).first()       
        if sale:
            sale.state = False
            sale.save()
            return Response({'message':'Venta eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe una venta con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    


    