""" Model Client"""
from django.db import models
from app.models.base import BaseModel


class Client(BaseModel):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nit = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=20)
    adress = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name='Client'
        verbose_name_plural='Clients'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"