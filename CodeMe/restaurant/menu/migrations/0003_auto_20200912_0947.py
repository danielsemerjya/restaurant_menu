# Generated by Django 3.1 on 2020-09-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200912_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]