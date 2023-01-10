"""fullwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('home', views.home, name='home'),
    path('holiday', views.holiday, name='holiday'),
    path('holidayPackage/<int:id>', views.holidayPackage, name='holidayPackage'),
    path('signup', views.signup, name='signup'),
    path('admin_signup', views.admin_signup, name='admin_signup'),
    path('registerAdmin', views.registerAdmin, name='registerAdmin'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('logout', views.logout, name='logout'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('hotels', views.hotels, name='hotels'),
    path('hotelDetails/<int:id>', views.hotelDetails, name='hotelDetails'),
    path('holidaySearch', views.holidaySearch, name='holidaySearch'),
    path('hotelSearch', views.hotelSearch, name='hotelSearch'),
    path('search', views.search, name='search'),
    path('booking_hotel_search', views.booking_hotel_search, name='booking_hotel_search'),
    path('bus', views.bus, name='bus'),
    path('flights', views.flights, name='flights'),
    path('flight_search', views.flight_search, name='flight_search'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_users_show', views.admin_users_show, name='admin_users_show'),
    path('admin_package_show', views.admin_package_show, name='admin_package_show'),
    path('admin_packageDays_show', views.admin_packageDays_show, name='admin_packageDays_show'),
    path('admin_hotel_show', views.admin_hotel_show, name='admin_hotel_show'),
    path('admin_hotelRoom_show', views.admin_hotelRoom_show, name='admin_hotelRoom_show'),
    path('admin_bus_show', views.admin_bus_show, name='admin_bus_show'),
    path('admin_state_show', views.admin_state_show, name='admin_state_show'),
    path('admin_city_show', views.admin_city_show, name='admin_city_show'),
    path('admin_user_update/<int:id>', views.admin_user_update, name='admin_user_update'),
    path('admin_package_update/<int:id>', views.admin_package_update, name='admin_package_update'),
    path('admin_user_edit/<int:id>', views.admin_user_edit, name='admin_user_edit'),
    path('admin_package_edit/<int:id>', views.admin_package_edit, name='admin_package_edit'),
    path('booking_package/<int:id>/', views.booking_package, name='booking_package'),
    path('booking_hotel/<int:id>/', views.booking_hotel, name='booking_hotel'),
    path('booking_hotel_type2/<int:id>/', views.booking_hotel_type2, name='booking_hotel_type2'),
    path('success', views.success, name='success'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('payment_hotel/<int:id>', views.payment_hotel, name='payment_hotel'),
    path('payment_hotel_type2/<int:id>', views.payment_hotel_type2, name='payment_hotel_type2'),
    path('booking_report', views.booking_report, name='booking_report'),
    path('booking_hotel_report', views.booking_hotel_report, name='booking_hotel_report'),
    # path('venue_pdf', views.venue_pdf, name='venue_pdf'),
]
