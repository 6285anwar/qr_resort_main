from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import datetime
from dateutil.relativedelta import relativedelta
import os







def login(request):
    return render(request,'login.html')

def admin_navbar(request):
    return render(request,'admin_navbar.html')

def admin_dashboard(request):

    
    resort = user_registration.objects.all().order_by('-id')

    sales_count = user_registration.objects.all().count()

    return render(request, 'admin_dashboard.html',{'resort':resort,'sales_count':sales_count})

def admin_services(request):
    if request.method == 'POST':
        s = services()
        s.service_name = request.POST['servicename']
        s.photo = request.FILES.get('image', None)
        s.save()
        return redirect(admin_services)
    service = services.objects.all()
    return render(request,'admin_services.html',{'service':service})

def admin_property(request):
    resort = user_registration.objects.all()
    return render(request,'admin_property.html',{'resort':resort})

def admin_create_property(request):
    service = services.objects.all()
    return render(request,'admin_create_property.html',{'service':service})

def admin_property_save(request):
    today = datetime.date.today()

    if request.method == 'POST':
        property_name = request.POST['pr']
        owner_name = request.POST['on']
        username = request.POST['un']
        password = request.POST['pswd']
        email = request.POST['email']
        phone = request.POST['ph']
        address = request.POST['ad']
        city = request.POST['cty']
        state = request.POST['st']
        country = request.POST['co']
        logo = request.FILES.get("image", False)
        agreement = request.FILES.get("agmt",False)
        duration = request.POST['du']
        amount = request.POST['amt']
        tax = request.POST['tax']
        total = request.POST['ttl']
        selected_service = request.POST.getlist('service[]')
        restaurant_phone = request.POST['r_ph']





        ur = user_registration()
        ur.fullname = property_name
        ur.owner_name = owner_name
        ur.username = username
        ur.password = password
        ur.email = email
        ur.mobile = phone
        ur.address = address
        ur.city = city
        ur.state = state
        ur.country = country
        ur.logo = logo
        ur.agreement = agreement
        ur.duration = duration
        ur.amount = amount
        ur.tax = tax
        ur.total = total
        ur.restaurant_mobile=restaurant_phone
        ur.Rooms = '0'
        ur.date = today
        ur.save()


        user_reg = user_registration.objects.get(id=ur.id)
        for i in selected_service:
            selected_services.objects.create(service_name=i, property_id=user_reg)

        ur.code_id = "Q6-" + \
            str(ur.id).zfill(5)
        ur.status = '-1'
        ur.save()
        

    
        return redirect('admin_dashboard')

def admin_manage_property(request,id):
    file = 'Error.png'
    user = user_registration.objects.get(id=id)
    roomqr = room_qr.objects.filter(property_id=id)

    qr = room_qr.objects.filter(qr_file_status='no_files').filter(property_id=id)

    for i in qr:
        i.qr_code = file
        i.save()

    


    return render(request,"admin_manage_property.html",{'user':user,'roomqr':roomqr})

def admin_property_activate(request,id):
    user = user_registration.objects.get(id=id)
    user.status = '1'
    user.startdate = datetime.date.today()

    print(user.duration)
    today = datetime.date.today()
    


    if user.duration == 0:
        three_days_later = today + datetime.timedelta(days=3)
        user.enddate = three_days_later
        user.save()
    elif user.duration == 1.0:
        one_months_later = today + relativedelta(months=1)
        user.enddate = one_months_later
        user.save()
    elif user.duration == 6.0:
        six_months_later = today + relativedelta(months=6)
        user.enddate = six_months_later
        user.save()
    elif user.duration == 12.0:
        one_year_later = today + relativedelta(months=12)
        user.enddate = one_year_later
        user.save()
    user.save()
    return redirect('admin_dashboard')

def admin_property_deactivate(request,id):
    user = user_registration.objects.get(id=id)
    user.status = '0'
    user.save()
    return redirect('admin_dashboard')

def admin_create_room(request,id):
    user = user_registration.objects.get(id=id)
    
    room_count = room_qr.objects.filter(property_id=id).count()
    print(room_count)
    return render(request,'admin_create_room.html',{'user':user})




def my_view(request):
    if request.method == 'POST':
        selected_states = request.POST.getlist('service[]')

        for i in selected_states:
            print(i)
    return redirect(admin_services)

def admin_room_qr_file_upload(request,id_value1):
    user = user_registration.objects.get(id=id_value1)
    id_pass=user.id
    
    qr = room_qr.objects.filter(property_id=user)
    

    return render(request,'admin_room_qr_file_upload.html',{'qr':qr,'id_value1':id_pass})


def admin_room_qr_file_upload_save(request,id):
    qr = room_qr.objects.get(id=id)
    room_id = qr.property_id.id
    if request.method == 'POST':
        qr_file = request.FILES.get("qr_file", False)
        qr.qr_code=qr_file
        qr.qr_file_status = 'file_uploded'
        qr.save()
    return redirect(reverse('admin_room_qr_file_upload', args=[room_id]))


def admin_room_qr_file_edit(request,id):
    qr = room_qr.objects.get(id=id)
    room_id = qr.property_id.id
    if request.method == 'POST':
       
        room = request.POST['room_no']
        url = request.POST['url']
        qr_file = request.FILES.get("qr", False)

        qr.room_number = room
        qr.qr_url = url
        qr.qr_code = qr_file

        if qr.qr_code == False:
            qr.qr_file_status = 'no_files'
        else:
            qr.qr_file_status = 'file_uploded'

        qr.save()

    return redirect(reverse('admin_manage_property', args=[room_id]))


    


   
    


















    
#==================== AJAX ===============
def validate(request):

    if request.method == 'GET':
        nick_name = request.GET['nick_name']
        if user_registration.objects.filter(username=nick_name).exists():
            return HttpResponse("Success!")

def admin_room_count(request):
    if request.method == 'GET':
        room_count = request.GET['nick_name']
        user = request.GET['user_id']
        main_user = user_registration.objects.get(id=user)
        main_user.Rooms = room_count
        main_user.save()   
        print("saved")
        return HttpResponse("Success!")



# def admin_room_number(request):
#     if request.method == 'GET':
#         room_count = request.GET['nick_name']
#         print("hi",room_count)
#         return HttpResponse("Success!")


# def admin_room_number(request):
#     if request.method == 'POST':
#         form_data = {
#             'room_no_1': request.POST.get('room_no_1'),
#             'room_no_2': request.POST.get('room_no_2')
#         }
#         for i in form_data:
#             if i.startswith('room_no_'):
#                 room_number = form_data[i]
#                 print(room_number)


#         return JsonResponse({'message': 'Form submitted successfully!'})

#     return JsonResponse({'error': 'Invalid request method.'}, status=405)

def admin_room_number(request):
    if request.method == 'POST':
        id_value1 = request.POST.get('id_value1')

        resort_room_count = user_registration.objects.get(id=id_value1)
        count = resort_room_count.Rooms
        cout = int(count)

        url = request.META.get('HTTP_REFERER')
        base_url = url.split("/", 3)[0] + "//" + url.split("/")[2] + "/"

        form_data = {}
        for i in range(1, cout+1):
            room_key = f'room_no_{i}'
            room_number = request.POST.get(room_key)
            if room_number:
                form_data[room_key] = room_number
                print(room_number)
                
                print(base_url)
             


                room = room_qr()
                room.property_id = resort_room_count
                room.room_number = room_number
                room.qr_url = base_url+"resort_qr/"+id_value1+"/"+room_number
                room.qr_file_status = 'no_files'
                room.save()
                


        return JsonResponse({'message': 'Form submitted successfully!'})

    return JsonResponse({'error': 'Invalid request method.'}, status=405)




























def resort_index(request):
    return render(request,'resort_index.html')



