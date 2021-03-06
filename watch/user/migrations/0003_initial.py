# Generated by Django 4.0.6 on 2022-07-07 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0002_productmodel_product_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_delete_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.productmodel')),
                ('user_if', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
