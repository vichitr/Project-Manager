# Generated by Django 2.0.1 on 2018-03-30 18:17

import classroom.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20180330_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to=classroom.models.user_directory_path)),
                ('projectid', models.IntegerField(default=0)),
            ],
        ),
    ]
