# Generated by Django 4.2.3 on 2025-07-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_placeimage_number'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='placeimage',
            index=models.Index(fields=['number'], name='places_plac_number_a294f0_idx'),
        ),
    ]
