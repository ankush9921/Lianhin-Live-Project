# Generated by Django 4.0.6 on 2023-09-18 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lianhin', '0004_rename_name_brand_brand_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='brand_id',
            new_name='brand',
        ),
    ]
