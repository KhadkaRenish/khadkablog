# Generated by Django 5.0.7 on 2024-07-22 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_abouts_remove_about_chooseus_remove_about_image_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="About",
        ),
        migrations.DeleteModel(
            name="Abouts",
        ),
    ]
