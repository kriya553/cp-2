# Generated by Django 4.1.4 on 2023-04-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_vendorregistration_delete_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorregistration',
            name='usertype',
            field=models.CharField(default='vendor', max_length=10),
        ),
    ]