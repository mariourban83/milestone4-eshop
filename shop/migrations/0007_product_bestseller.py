# Generated by Django 3.0.4 on 2020-04-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200331_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bestseller',
            field=models.BooleanField(default=False),
        ),
    ]
