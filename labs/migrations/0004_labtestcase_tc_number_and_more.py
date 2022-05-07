# Generated by Django 4.0.4 on 2022-05-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_labanswer_unique_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestcase',
            name='tc_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='labquestion',
            name='question_number',
            field=models.PositiveIntegerField(),
        ),
    ]
