# Generated by Django 4.2.6 on 2023-10-24 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailSale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cant', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sale')),
            ],
            options={
                'verbose_name': 'Detalle_Venta',
                'verbose_name_plural': 'Detalle_Ventas',
            },
        ),
    ]
