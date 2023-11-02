""" Model Base """

from django.db import models


class BaseModel(models.Model):

    id=models.AutoField(primary_key=True)
    state=models.BooleanField('Estado',default=True)
    create_date=models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True)
    modified_date=models.DateField('Fecha de Modificacion',auto_now=True,auto_now_add=False)
    delete_date=models.DateField('Fecha de Eliminacion',auto_now=True,auto_now_add=False)

    class Meta:
        abstract=True
        verbose_name='Modelo Base'
        verbose_name_plural='Modelos Base'


class MeasureUnit(BaseModel):

    description=models.CharField('Descripcion', max_length=50,blank=False,null=False,unique=True)

    class Meta:
        verbose_name='Unidad de Medida'
        verbose_name_plural='Unidades de Medidas'

    def __str__(self):
        return self.description
    