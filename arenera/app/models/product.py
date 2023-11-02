from django.db import models
from app.models.base import BaseModel,MeasureUnit
    
class Product(BaseModel):

    description=models.CharField('Descripcion', max_length=50,blank=False,null=False)
    image=models.ImageField('Imagen del Producto',upload_to='products/',blank=True,null=True)
    measure_unit=models.ForeignKey(MeasureUnit,on_delete=models.CASCADE,verbose_name='Unidad de Medida',null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def __str__(self):
        return self.description