# Generated by Django 4.2.3 on 2023-09-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('Topic_Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
