# Generated by Django 5.0.4 on 2024-05-06 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_description_event_is_online'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventcomment',
            options={'verbose_name': ('Comment',), 'verbose_name_plural': 'Event comments'},
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
        migrations.AlterField(
            model_name='eventcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]