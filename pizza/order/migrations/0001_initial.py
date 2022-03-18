# Generated by Django 3.2.8 on 2022-03-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('delivery_status', models.CharField(choices=[('PEN', 'Pending'), ('DEL', 'Delivered')], default='PEN', max_length=3)),
                ('pizza_order', models.ManyToManyField(to='pizza.PizzaModel')),
            ],
            options={
                'verbose_name': 'Orders',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
