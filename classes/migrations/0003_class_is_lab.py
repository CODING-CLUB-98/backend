# Generated by Django 4.0.4 on 2022-05-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='is_lab',
            field=models.BooleanField(default=False),
        ),
    ]