# Generated by Django 5.0.7 on 2024-08-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0003_adminlogin_alter_masterlogin_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=255)),
                ('server_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='adminlogin',
        ),
    ]
