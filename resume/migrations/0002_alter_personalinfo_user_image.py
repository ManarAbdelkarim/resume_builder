# Generated by Django 3.2.6 on 2021-08-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='user_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
