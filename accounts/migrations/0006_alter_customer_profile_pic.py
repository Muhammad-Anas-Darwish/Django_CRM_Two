# Generated by Django 3.2.13 on 2022-04-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
