# Generated by Django 4.2.1 on 2023-05-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRSTAY_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=240, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]