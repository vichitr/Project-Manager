# Generated by Django 2.0.1 on 2018-03-30 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='report',
            new_name='file',
        ),
    ]
