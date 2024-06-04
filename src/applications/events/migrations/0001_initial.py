# Generated by Django 5.0.4 on 2024-06-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('reference', models.CharField(max_length=255)),
                ('reference_video', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/%Y/%m/%d')),
                ('is_online', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': ('Comment',),
                'verbose_name_plural': 'Event comments',
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'Registered'), (1, 'Arrived'), (2, 'Skipped'), (3, 'Canceled')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
