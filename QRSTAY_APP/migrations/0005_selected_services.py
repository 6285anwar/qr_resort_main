# Generated by Django 4.2.1 on 2023-05-14 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QRSTAY_APP', '0004_user_registration_owner_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='selected_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=240, null=True)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QRSTAY_APP.user_registration')),
            ],
        ),
    ]
