# Generated by Django 4.0.6 on 2023-09-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lianhin', '0007_rename_brand_id_collection_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_image',
            field=models.FileField(blank=True, null=True, upload_to='brand'),
        ),
    ]
