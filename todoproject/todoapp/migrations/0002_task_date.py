# Generated by Django 4.2.2 on 2023-07-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-08-23'),
            preserve_default=False,
        ),
    ]
