# Generated by Django 4.2.1 on 2023-05-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRSTAY_APP', '0002_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='Rooms',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='agreement',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='code_id',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='duration',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='email',
            field=models.EmailField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='facebook_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='insta_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='logo',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='mobile',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='property_name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='restaurant_mobile',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='tax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='twitter_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='website',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='youtube_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
