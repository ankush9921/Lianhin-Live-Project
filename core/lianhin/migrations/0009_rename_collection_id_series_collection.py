# Generated by Django 4.0.6 on 2023-09-18 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lianhin', '0008_brand_brand_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='collection_id',
            new_name='collection',
        ),
    ]