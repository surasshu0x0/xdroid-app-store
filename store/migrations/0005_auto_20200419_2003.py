# Generated by Django 3.0.5 on 2020-04-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200419_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='mini_description',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
