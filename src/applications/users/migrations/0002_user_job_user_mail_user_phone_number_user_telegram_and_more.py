# Generated by Django 5.0.4 on 2024-04-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='vk',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
