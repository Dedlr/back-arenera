from django.db import models
from django.core.validators import MinValueValidator
from app.models.client import Client  # Import your Client model
from app.models.product import Product  # Import your Product model
from app.models.user import User  # Import your User model
from app.models.sale import Sale

class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)

    def save(self, *args, **kwargs):
        self.subtotal = self.price * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles Ventas'

    def _str_(self):
        return f"Detalle de Venta {self.sale.id} - {self.product.description}"