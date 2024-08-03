# Generated by Django 4.0 on 2024-08-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=20)),
                ('releasedate', models.DateField()),
                ('heroname', models.CharField(max_length=20)),
                ('heroinename', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
