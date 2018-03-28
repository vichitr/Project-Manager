# Generated by Django 2.0.1 on 2018-03-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0009_auto_20180328_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cls',
            field=models.CharField(choices=[('a', 'B. Tech'), ('b', 'M. Tech'), ('c', 'MCA'), ('d', 'PhD')], max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('a', 'Department of Computer Science and Engineering'), ('b', 'Department of Information Technology'), ('c', 'Department of Electronics & Communication Engineering'), ('d', 'Department of Electrical and Electronics Engineering'), ('e', 'Department of Mechanical Engineering'), ('f', 'Department of Civil Engineering'), ('g', 'Department of Mathematical and Computational Sciences'), ('h', 'Department of Mining Engineering'), ('i', 'Department of Chemical Engineering'), ('j', 'Department of Metallurgical and Materials Engineering'), ('k', 'Department of Applied Mechanics and Hydraulics'), ('l', 'Department of Physics'), ('m', 'Department of Chemistry'), ('n', 'Department of Placement and Training'), ('o', 'School of Management')], max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1),
        ),
    ]
