from django.contrib import admin
from django.urls import path
from QRSTAY_APP import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_navbar',views.admin_navbar,name="admin_navbar"),
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('admin_services',views.admin_services,name="admin_services"),
    path('admin_property',views.admin_property,name="admin_property"),
    path('admin_create_property',views.admin_create_property,name="admin_create_property"),
    path('admin_property_save',views.admin_property_save,name="admin_property_save"),
    path('admin_manage_property/<int:id>',views.admin_manage_property,name="admin_manage_property"),
    path('admin_property_activate/<int:id>',views.admin_property_activate,name="admin_property_activate"),
    path('admin_property_deactivate/<int:id>',views.admin_property_deactivate,name="admin_property_deactivate"),
    path('admin_create_room/<int:id>',views.admin_create_room,name="admin_create_room"),
    path('admin_room_qr_file_upload/<int:id_value1>',views.admin_room_qr_file_upload,name="admin_room_qr_file_upload"),

    path('admin_room_qr_file_upload_save/<int:id>',views.admin_room_qr_file_upload_save,name="admin_room_qr_file_upload_save"),
    path('admin_room_qr_file_edit/<int:id>',views.admin_room_qr_file_edit,name="admin_room_qr_file_edit"),





    



   #==================== A J A X ===================#
    path('validate', views.validate, name = "validate"),
    path('admin_room_count',views.admin_room_count,name="admin_room_count"),
    path('admin_room_number',views.admin_room_number,name="admin_room_number"),




    path('',views.login,name="login"),

    path('my_view',views.my_view,name="my_view"),

    path('resort_index',views.resort_index,name="resort_index"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)