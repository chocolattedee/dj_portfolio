# Generated by Django 4.2.5 on 2023-09-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.FileField(blank=True, upload_to='home_images/'),
        ),
    ]
