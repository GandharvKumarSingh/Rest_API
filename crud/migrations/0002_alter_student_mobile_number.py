# Generated by Django 3.2.5 on 2021-08-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(max_length=50),
        ),
    ]
