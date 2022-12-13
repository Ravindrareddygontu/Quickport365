"""cargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from service import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('', views.base, name='base'),
    path('hom', views.home, name='home'),
    path('booking', views.booking,name='book'),
    path('trac/',views.tracking,name='trac'),
    path('profiles', views.profiles, name='profiles'),
    path('sign', views.sign, name='signup'),
    path('log_in', views.logins, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('parcel', views.parcel, name='parcel'),
    path('summary', views.order_summary, name='summary'),
    path('payment', views.payment_details, name='payment'),
    path('address', views.address_enter, name='address'),
    path('payment_options', views.payment_options, name='payment_options'),
    path('success', views.success, name='success'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('success', views.success, name='success'),
    path('histor', views.history, name='history'),
    path('api/register', views.RegisterView.as_view(), name='api_register'),
    path('api/login', views.LoginView.as_view(), name='api_login'),
    path('api/user', views.UserView.as_view(), name='api_user'),
    path('driver_dashboard', views.driver_dashboard, name='driver'),
    path('edit/<int:id>/', views.edit_order, name='edit'),
    path('complaint', views.complaint, name='complaint'),
    path('drivers', views.list_drivers, name='drivers'),
    path('usercomplaints', views.user_complaints, name='usercomplaints'),
    path('orderspicked', views.orders_picked, name='orderspicked'),
    path('update_status/<int:id>', views.update_status, name='updatestatus'),
    path('complaint_order/<int:id>', views.complaint_order, name='complaint_order'),
    path('admin_driver', views.admin_driver, name='admin_driver'),
    path('driver_details/<int:id>/', views.driver_details, name='driver_details'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)