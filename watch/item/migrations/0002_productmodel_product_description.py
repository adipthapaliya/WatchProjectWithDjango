# Generated by Django 4.0.6 on 2022-07-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_description',
            field=models.TextField(default='No Description Avilable', max_length=225),
        ),
    ]
