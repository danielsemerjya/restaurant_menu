# Generated by Django 3.1 on 2020-09-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20200912_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]