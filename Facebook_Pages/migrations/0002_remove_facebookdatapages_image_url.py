# Generated by Django 3.0.8 on 2020-07-07 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook_Pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookdatapages',
            name='image_url',
        ),
    ]
