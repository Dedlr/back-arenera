from django.db import models
from django.core.validators import MinValueValidator
from app.models.client import Client 
from app.models.user import User  

class Sale(models.Model):
    date = models.DateField('Fecha', auto_now=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00)])
    cancel=models.BooleanField('Cancelado',default=True)
    state=models.BooleanField('Estado',default=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def _str_(self):
        return f"Venta {self.id}"