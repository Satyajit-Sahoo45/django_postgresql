# Generated by Django 4.2.5 on 2023-09-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgre_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('depi_id', models.CharField(max_length=255, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
