# Generated by Django 5.1.4 on 2025-01-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lindomar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charcaters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('house', models.CharField(max_length=200)),
                ('wizard', models.BooleanField()),
                ('eyeColor', models.CharField(max_length=200)),
                ('hairColor', models.CharField(max_length=200)),
                ('actor', models.CharField(max_length=200)),
                ('image', models.TextField()),
            ],
        ),
    ]
