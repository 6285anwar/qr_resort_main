from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.


class user_registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    owner_name = models.CharField(max_length=240, null=True)



    code_id = models.CharField(max_length=80 ,null=True)
    
    password = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=240, null=True)
    mobile = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    logo = models.FileField(upload_to="media", null=True)
    amount = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    total = models.FloatField(null=True)
    duration = models.FloatField(max_length=10,null=True)
    restaurant_mobile = models.CharField(max_length=50, null=True)
    agreement = models.FileField(upload_to="media", null=True)
    status = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    website = models.CharField(max_length=200, null=True)
    insta_id = models.CharField(max_length=200, null=True)
    facebook_id = models.CharField(max_length=200, null=True)
    twitter_id = models.CharField(max_length=200, null=True)
    youtube_id = models.CharField(max_length=200, null=True)

    Rooms = models.CharField(null=True,max_length=10)



class selected_services(models.Model):
    property_id = models.ForeignKey(user_registration, on_delete=CASCADE)
    service_name = models.CharField(max_length=240, null=True)



class room_qr(models.Model):
    property_id = models.ForeignKey(user_registration, on_delete=CASCADE)
    room_number = models.CharField(max_length=240, null=True)
    qr_url = models.CharField(max_length=240, null=True)
    qr_code = models.FileField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True)
    qr_file_status = models.CharField(max_length=240, null=True)

















class services(models.Model):
    service_name = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
