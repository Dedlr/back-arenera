from django.contrib import admin
from app.models.client import Client
from app.models.base import MeasureUnit
from app.models.product import Product
from app.models.user import User
from app.models.sale import Sale
from app.models.detail_sale_product import DetailSale
#Model Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','nit')

admin.site.register(Client,ClientAdmin)

#MeasureUnit
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(MeasureUnit,MeasureUnitAdmin)

#Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','description','price')
admin.site.register(Product,ProductAdmin)

#@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','category')
admin.site.register(User)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id','date','client','user')

admin.site.register(Sale,SaleAdmin)


class DetailAdmin(admin.ModelAdmin):
    list_display = ('id','sale','product')

admin.site.register(DetailSale,DetailAdmin)
