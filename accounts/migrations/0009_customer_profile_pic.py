# Generated by Django 3.1.2 on 2020-11-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
