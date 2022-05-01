# Generated by Django 4.0.4 on 2022-04-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_code',
            field=models.CharField(max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='sem',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_code',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]