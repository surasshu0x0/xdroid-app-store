# Generated by Django 3.0.5 on 2020-04-19 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200419_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='suppport_url',
            new_name='support_url',
        ),
    ]
