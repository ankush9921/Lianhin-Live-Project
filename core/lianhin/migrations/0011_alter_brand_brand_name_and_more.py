# Generated by Django 4.0.6 on 2023-09-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lianhin', '0010_model_alter_collection_collection_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='surfacefinish',
            name='surface_name',
            field=models.CharField(max_length=255),
        ),
    ]
