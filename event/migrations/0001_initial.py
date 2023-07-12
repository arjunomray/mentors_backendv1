# Generated by Django 4.0.4 on 2023-07-11 17:12

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
                ('event_name', models.CharField(max_length=20)),
                ('poster', models.URLField()),
                ('registration_link', models.URLField(max_length=100)),
                ('time', models.DateField()),
                ('event_summary', models.TextField()),
            ],
        ),
    ]