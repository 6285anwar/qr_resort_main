# Generated by Django 4.2.1 on 2023-05-15 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QRSTAY_APP', '0005_selected_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration',
            name='property_name',
        ),
    ]