# Generated by Django 3.0.4 on 2020-04-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200402_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(default='Content : '),
        ),
    ]
