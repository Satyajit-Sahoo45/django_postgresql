# Generated by Django 4.2.5 on 2023-09-18 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postgre_app', '0002_dept_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('RollNumber', models.CharField(default=None, max_length=255)),
                ('branch', models.CharField(default=None, max_length=255)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgre_app.dept')),
            ],
        ),
    ]
