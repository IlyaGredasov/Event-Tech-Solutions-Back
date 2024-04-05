# Generated by Django 5.0.4 on 2024-04-11 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'Sent'), (1, 'Delivered'), (2, 'Read')])),
                ('time', models.DateTimeField()),
                ('description', models.TextField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_notifications', to='events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
