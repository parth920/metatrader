# Generated by Django 5.0.7 on 2024-08-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_server_delete_adminlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterlogin',
            name='pin',
            field=models.CharField(default=2011, max_length=6),
            preserve_default=False,
        ),
    ]
