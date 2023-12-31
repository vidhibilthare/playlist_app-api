# Generated by Django 4.1.7 on 2023-06-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songname', models.CharField(max_length=150)),
                ('songimage', models.ImageField(upload_to='image')),
                ('songaudio', models.FileField(upload_to='audio')),
                ('singer', models.CharField(max_length=200)),
                ('songmoviename', models.CharField(default=None, max_length=200)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
