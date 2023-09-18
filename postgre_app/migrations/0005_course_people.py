# Generated by Django 4.2.5 on 2023-09-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgre_app', '0004_rename_rollnumber_student_rollnumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('courses', models.ManyToManyField(to='postgre_app.course')),
            ],
        ),
    ]