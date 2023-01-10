from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.sessions.models import Session
from .forms import *
import razorpay
from django.views.decorators.csrf import csrf_exempt


def login(request):
    if request.session.has_key('is_login'):
        return redirect('home')

    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        count=User.objects.filter(username=username,password=password).count()
        if count>0:
            # u_name=request.session.username
            request.session['is_login']=True
            # return HttpResponse("User Login Done")
            return redirect('home')
        else:
            messages.error(request,"Wrong Id or Password!")
            return redirect('login')
    return render(request,'login.html')

def admin_login(request):
    if request.session.has_key('is_admin_login'):
        return redirect('admin_home')

    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        count=Admin.objects.filter(username=username,password=password).count()
        if count>0:
            # u_name=request.session.username
            request.session['is_admin_login']=True
            # return HttpResponse("User Login Done")
            return redirect('admin_home')
        else:
            messages.error(request,"Wrong Id or Password!")
            return redirect('admin_login')
    return render(request,'admin_login.html')

def admin_home(request):
    if request.session.has_key('is_admin_login'):
        return render(request,'admin_home.html')
    return redirect('admin_login')

def admin_signup(request):
    return render(request,'admin_signup.html')

def signup(request):
    return render(request,'signup.html')

def registerAdmin(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        obj=Admin(username=username,email=email,password=password)
        obj.save()
        messages.success(request,"Admin Resistered Successfully!")
        return redirect('admin_login')

def registerUser(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        obj=User(username=username,email=email,password=password)
        obj.save()
        messages.success(request,"User Resistered Successfully!")
        return redirect('login')

def booking_package(request,id):
    if request.session.has_key('is_login'):
        data = Package_Master.objects.get(id=id)
        data3 = Package_Days.objects.get(id=id)
        data2 = Package_Master.objects.all()
        return render(request,'booking_package.html',{'data':data,'data2':data2,'data3':data3})
    return redirect('login')

def payment(request,id):
    if request.session.has_key('is_login'):
        if request.POST:
            amount=50000
            order_currency = 'INR'
            client = razorpay.Client(
                auth=('rzp_test_j6zKRXbm19WPTB','lxx3Gm7ku36wtWnNOVxYwLj1')
            )
            payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})

        if request.POST:
            fullname=request.POST['fullname']
            pack_name=request.POST['pack_name']
            pack_price=request.POST['pack_price']
            email=request.POST['email']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            zipcode=request.POST['zipcode']
            rooms=request.POST['rooms']
            adults=request.POST['adults']
            dob=request.POST['dob']
            obj=Booking_Package(fullname=fullname,email=email,address=address,
                                city=city,state=state,zipcode=zipcode,rooms=rooms,
                                adults=adults,dob=dob,pack_name=pack_name,pack_price=pack_price)
            obj.save()
        data=Package_Master.objects.all()
        data2=Package_Master.objects.get(id=id)
        return render(request,'payment.html',{'data2':data2,'data':data})
    return redirect('login')

def payment_hotel(request,id):
    if request.session.has_key('is_login'):
        if request.POST:
            amount=50000
            order_currency = 'INR'
            client = razorpay.Client(
                auth=('rzp_test_j6zKRXbm19WPTB','lxx3Gm7ku36wtWnNOVxYwLj1')
            )
            payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})

        if request.POST:
            fullname=request.POST['fullname']
            hotel_id= Hotel_Room.objects.get(id=id)
            room_name=request.POST['room_name']
            room_price_type_1=request.POST['room_price_type_1']
            room_price_type_2=request.POST['room_price_type_2']
            email=request.POST['email']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            zipcode=request.POST['zipcode']
            rooms=request.POST['rooms']
            adults=request.POST['adults']
            dob=request.POST['dob']
            obj=Booking_Hotel(fullname=fullname,email=email,address=address,
                                city=city,state=state,zipcode=zipcode,rooms=rooms,
                                adults=adults,dob=dob,room_name=room_name,room_price_type_1=room_price_type_1,
                                room_price_type_2=room_price_type_2,hotel_id=hotel_id)
            obj.save()
        data=Hotel_Room.objects.all()
        data2=Hotel_Room.objects.get(id=id)
        return render(request,'payment_hotel.html',{'data2':data2,'data':data})
    return redirect('login')

def payment_hotel_type2(request,id):
    if request.session.has_key('is_login'):
        if request.POST:
            amount=50000
            order_currency = 'INR'
            client = razorpay.Client(
                auth=('rzp_test_j6zKRXbm19WPTB','lxx3Gm7ku36wtWnNOVxYwLj1')
            )
            payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})

        if request.POST:
            hotel_id = Hotel_Room.objects.get(id=id)
            fullname=request.POST['fullname']
            room_name=request.POST['room_name']
            room_price_type_1=request.POST['room_price_type_1']
            room_price_type_2=request.POST['room_price_type_2']
            email=request.POST['email']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            zipcode=request.POST['zipcode']
            rooms=request.POST['rooms']
            adults=request.POST['adults']
            dob=request.POST['dob']
            obj=Booking_Hotel(fullname=fullname,email=email,address=address,
                                city=city,state=state,zipcode=zipcode,rooms=rooms,
                                adults=adults,dob=dob,room_name=room_name,room_price_type_1=room_price_type_1,
                                room_price_type_2=room_price_type_2,hotel_id=hotel_id)
            obj.save()
        data=Hotel_Room.objects.all()
        data2=Hotel_Room.objects.get(id=id)
        return render(request,'payment_hotel_type2.html',{'data2':data2,'data':data})
    return redirect('login')

def home(request):
    if request.session.has_key('is_login'):
        data = Package_Master.objects.all()
        return render(request,'home.html',{'data':data})
    return redirect('login')

def logout(request):
    del request.session['is_login']
    return redirect('login')

def admin_logout(request):
    del request.session['is_admin_login']
    return redirect('admin_login')

def holiday(request):
    if request.session.has_key('is_login'):
        data=Package_Master.objects.all()
        return render(request,'holiday.html',{'data':data})
    return redirect('login')

def holidayPackage(request,id):
    if request.session.has_key('is_login'):
        data2 = Package_Days.objects.filter(package_master_id=id)
        data = Package_Master.objects.get(id=id)
        data3 = Package_Master.objects.all()
        return render(request, 'holidayPackage.html', {'data':data,'data2':data2,'data3':data3})
    return redirect('login')





def hotels(request):
    if request.session.has_key('is_login'):
        data=Hotel_Master.objects.all()
        return render(request,'hotels.html',{'data':data})
    return redirect('login')

def hotelDetails(request,id):
    if request.session.has_key('is_login'):
        data=Hotel_Master.objects.get(id=id)
        data2=Hotel_Room.objects.filter(hotel_master_id=id)
        data3=Hotel_Room.objects.all()
        return render(request,'hotelDetails.html',{'data':data,'data2':data2,'data3':data3})
    return redirect('login')

def booking_hotel(request,id):
    if request.session.has_key('is_login'):
        data2 = Hotel_Room.objects.get(id=id)
        data = request.user
        return render(request, 'booking_hotel.html',{'data2':data2,'data':data})
    return redirect('login')

def booking_hotel_type2(request,id):
    if request.session.has_key('is_login'):
        data2 = Hotel_Room.objects.get(id=id)
        return render(request, 'booking_hotel_type2.html',{'data2':data2})
    return redirect('login')



def holidaySearch(request):
    if request.session.has_key('is_login'):
        searched = request.POST['searched']
        data = Package_Master.objects.filter(pack_name__contains=searched)
        return render(request,'holidaySearch.html',{'searched':searched,'data':data})
    return redirect('login')


def hotelSearch(request):
    if request.session.has_key('is_login'):
        searched = request.POST['searched']
        data = Hotel_Master.objects.filter(hotel_details__contains=searched)
        return render(request,'hotelSearch.html',{'searched':searched,'data':data})
    return redirect('login')

def flights(request):
    if request.session.has_key('is_login'):
        destination = request.POST['destination']
        departure = request.POST['departure']

        data = Flights_master.objects.filter(departure__contains=departure).filter(destination__contains=destination)
        # data = Flights_master.objects.filter(departure__contains=departure)
        return render(request,'flights.html',{'data':data,'departure':departure})
    return redirect('login')

def flight_search(request):
    if request.session.has_key('is_login'):

        return render(request,'flight_search.html')
    return redirect('login')



def bus(request):
    if request.session.has_key('is_login'):
        data = Bus_master.objects.all()
        return render(request,'bus.html',{'data':data})
    return redirect('login')





def admin_users_show(request):
    data=User.objects.all()
    return render(request,'users/admin_users_show.html',{'data':data})

def admin_package_show(request):
    data=Package_Master.objects.all()
    return render(request,'holiday_package/admin_package_show.html',{'data':data})

def admin_packageDays_show(request):
    data=Package_Days.objects.all()
    return render(request,'holiday_package/admin_packageDays_show.html',{'data':data})

def admin_hotel_show(request):
    data=Hotel_Master.objects.all()
    return render(request,'hotel/admin_hotel_show.html',{'data':data})

def admin_hotelRoom_show(request):
    data=Hotel_Room.objects.all()
    return render(request,'hotel/admin_hotelRoom_show.html',{'data':data})

def admin_bus_show(request):
    data=Bus_master.objects.all()
    return render(request,'bus/admin_bus_show.html',{'data':data})

def admin_state_show(request):
    data=State.objects.all()
    return render(request,'state/admin_state_show.html',{'data':data})

def admin_city_show(request):
    data=City.objects.all()
    return render(request,'city/admin_city_show.html',{'data':data})

def admin_user_update(request,id):
    data=User.objects.get(id=id)
    form=UserForm(request.POST,instance=data)
    form.save()
    return redirect('admin_users_show')

def admin_user_edit(request,id):
    data=User.objects.get(id=id)
    return render(request,'users/admin_user_edit.html',{'data':data})

def admin_package_update(request,id):
    data=Package_Master.objects.get(id=id)
    form=PackageForm(request.POST,instance=data)
    form.save()
    return redirect('admin_package_show')

def admin_package_edit(request,id):
    data=Package_Master.objects.get(id=id)
    return render(request,'holiday_package/admin_package_edit.html',{'data':data})


def search(request):
    searched = request.POST['searched']
    data = Booking_Package.objects.filter(fullname__contains=searched)
    return render(request,'search.html',{'data':data,'searched':searched})


def booking_report(request):
    data=Booking_Package.objects.all()
    return render(request,'users/booking_report.html',{'data':data})

def booking_hotel_report(request):
    data=Booking_Hotel.objects.all()
    return render(request,'users/booking_hotel_report.html',{'data':data})


def booking_hotel_search(request):
    searched = request.POST['searched']
    data = Booking_Hotel.objects.filter(dob__contains=searched)
    return render(request,'booking_hotel_search.html',{'data':data,'searched':searched})




@csrf_exempt
def success(request):
    return render(request,'success.html')