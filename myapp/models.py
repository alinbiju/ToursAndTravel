from django.db import models
from datetime import date

class User(models.Model):
    username=models.CharField('username',max_length=100)
    email=models.EmailField('email')
    password=models.CharField('password',max_length=20)

class Admin(models.Model):
    username=models.CharField('username',max_length=50)
    email=models.EmailField('email')
    password=models.CharField('password',max_length=20)

class State(models.Model):
    state_name=models.CharField('state_name',max_length=50)

class City(models.Model):
    city_name=models.CharField('city_name',max_length=50)
    city_pincode=models.IntegerField('city_pincode')
    state_id=models.ForeignKey(State,on_delete=models.CASCADE,default=1)

class Hotel_Master(models.Model):
    hotel_name=models.CharField('hotel_name',max_length=50)
    city_id=models.ForeignKey(City,on_delete=models.CASCADE)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',default='insert image')
    image2=models.ImageField(upload_to='images/',default='insert image')
    image3=models.ImageField(upload_to='images/',default='insert image')
    price=models.IntegerField('price',default=4900)
    check_in=models.CharField('check_in',max_length=10)
    check_out=models.CharField('check_out',max_length=10)
    hotel_details=models.CharField('hotel_details',max_length=1000)

class Package_Master(models.Model):
    pack_name=models.CharField('pack_name',max_length=50)
    destination=models.CharField('destination',max_length=50,default='AaBbCc')
    pack_details=models.CharField('pack_details',max_length=300)
    pack_price=models.IntegerField('pack_price')
    image=models.ImageField(upload_to='images/')
    image1=models.ImageField(upload_to='images/',default='asda')
    image2=models.ImageField(upload_to='images/',default='asda')
    image3=models.ImageField(upload_to='images/',default='asda')
    days=models.CharField('days',max_length=10,default='1')
    nights=models.CharField('nights',max_length=10,default='1')
    city_id=models.ForeignKey(City,on_delete=models.CASCADE,default=1)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE,default=1)

    # cit_id=models.ForeignKey(city,on_delete=models.CASCADE)
    # transportation_id=models.ForeignKey(transport_master,on_delete=models.CASCADE)

class Package_Days(models.Model):
    package_master_id=models.ForeignKey(Package_Master,on_delete=models.CASCADE)
    day = models.IntegerField('day', default=0)
    hotel_img = models.ImageField(upload_to='images/', default='asda')
    hotel_name = models.CharField('hotel_name', max_length=50, default='asda')
    hotel_id = models.ForeignKey(Hotel_Master, on_delete=models.CASCADE, default=1)
    sightseeing = models.CharField('sightseeing', max_length=40, blank=True)
    sightseeing1 = models.CharField('sightseeing1', max_length=40, blank=True)
    sightseeing2 = models.CharField('sightseeing2', max_length=40, blank=True)
    sightseeing3 = models.CharField('sightseeing3', max_length=40, blank=True)
    meal = models.CharField('meal', max_length=20, default='2')





class Hotel_Room(models.Model):
    room_name=models.CharField('room_name',max_length=50)
    # room type
    room_type_1=models.CharField('room_type_1',max_length=50,blank=True)
    room_type_2=models.CharField('room_type_2',max_length=50,blank=True)
    # max guest type
    max_guest_1=models.CharField('max_guest_1',max_length=50,blank=True)
    max_guest_2=models.CharField('max_guest_2',max_length=50,blank=True)
    # amenities
    amenities_1=models.CharField('amenities_1',max_length=15,blank=True)
    amenities_2=models.CharField('amenities_2',max_length=15,blank=True)
    amenities_3=models.CharField('amenities_3',max_length=15,blank=True)
    amenities_4=models.CharField('amenities_4',max_length=15,blank=True)
    amenities_5=models.CharField('amenities_5',max_length=15,blank=True)
    # inclusions type 1
    inclusions_type_1_1=models.CharField('inclusions_type_1_1',max_length=35,blank=True)
    inclusions_type_1_2=models.CharField('inclusions_type_1_2',max_length=35,blank=True)
    inclusions_type_1_3=models.CharField('inclusions_type_1_3',max_length=35,blank=True)
    inclusions_type_1_4=models.CharField('inclusions_type_1_4',max_length=35,blank=True)
    inclusions_type_1_5=models.CharField('inclusions_type_1_5',max_length=35,blank=True)
    # inclusions type 2
    inclusions_type_2_1=models.CharField('inclusions_type_2_1',max_length=35,blank=True)
    inclusions_type_2_2=models.CharField('inclusions_type_2_2',max_length=35,blank=True)
    inclusions_type_2_3=models.CharField('inclusions_type_2_3',max_length=35,blank=True)
    inclusions_type_2_4=models.CharField('inclusions_type_2_4',max_length=35,blank=True)
    inclusions_type_2_5=models.CharField('inclusions_type_2_5',max_length=35,blank=True)
    # highlights type 1
    highlights_type_1_1=models.CharField('highlights_type_1_1',max_length=65,blank=True)
    highlights_type_1_2=models.CharField('highlights_type_1_2',max_length=65,blank=True)
    highlights_type_1_3=models.CharField('highlights_type_1_3',max_length=65,blank=True)
    highlights_type_1_4=models.CharField('highlights_type_1_4',max_length=65,blank=True)
    highlights_type_1_5=models.CharField('highlights_type_1_5',max_length=65,blank=True)
    # highlights type 2
    highlights_type_2_1=models.CharField('highlights_type_2_1',max_length=65,blank=True)
    highlights_type_2_2=models.CharField('highlights_type_2_2',max_length=65,blank=True)
    highlights_type_2_3=models.CharField('highlights_type_2_3',max_length=65,blank=True)
    highlights_type_2_4=models.CharField('highlights_type_2_4',max_length=65,blank=True)
    highlights_type_2_5=models.CharField('highlights_type_2_5',max_length=65,blank=True)
    # room_price type 1
    room_price_type_1=models.IntegerField('room_price_type_1',blank=True)
    room_price_type_2=models.IntegerField('room_price_type_2',blank=True)
    # image type
    image_1=models.ImageField(upload_to='image/',default='Insert Image')
    # foriegn key hotel master
    hotel_master_id=models.ForeignKey(Hotel_Master,on_delete=models.CASCADE)

class Bus_master(models.Model):
    bus_name=models.CharField('bus_name',max_length=50)
    departure=models.CharField('departure',max_length=20)
    destination=models.CharField('destination',max_length=20,blank=True)
    duration=models.CharField('duration',max_length=10)
    departure_time = models.CharField('departure_time', max_length=50,blank=True)
    arrival=models.CharField('arrival',max_length=10,blank=True)
    price=models.CharField('price',max_length=10)
    seat_left=models.CharField('seat_left',max_length=10)

class Flights_master(models.Model):
    flight_name = models.CharField('flight_name', max_length=50)
    departure = models.CharField('departure', max_length=20)
    destination = models.CharField('destination', max_length=20, blank=True)
    duration = models.CharField('duration', max_length=10)
    departure_time = models.CharField('departure_time', max_length=50, blank=True)
    arrival = models.CharField('arrival', max_length=10, blank=True)
    price = models.CharField('price', max_length=10)
     # = models.CharField('seat_left', max_length=10)

class Booking_Package(models.Model):
    pack_name=models.CharField('pack_name',max_length=50)
    fullname=models.CharField('fullname',max_length=30)
    email=models.EmailField('email')
    address=models.CharField('address',max_length=200)
    city=models.CharField('city',max_length=30)
    state=models.CharField('state',max_length=30)
    zipcode=models.CharField('zipcode',max_length=30, default='38001')
    rooms=models.IntegerField('rooms')
    pack_price=models.IntegerField('pack_price',null=True)
    adults = models.IntegerField('adults', default=2)
    dob = models.DateField('dob', default=date.today)

class Booking_Hotel(models.Model):
    hotel_id=models.ForeignKey(Hotel_Room,on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', null=True)
    fullname = models.CharField('fullname', max_length=30, null=True)
    email = models.EmailField('email', null=True)
    address = models.CharField('address', max_length=200, null=True)
    city = models.CharField('city', max_length=30, null=True)
    state = models.CharField('state', max_length=30, null=True)
    zipcode = models.CharField('zipcode', max_length=30,blank=True)
    rooms = models.IntegerField('rooms', null=True)
    adults = models.IntegerField('adults', default=2)
    dob = models.DateField('dob', default=date.today)
    room_price_type_1 = models.IntegerField('room_price_type_1', null=True)
    room_price_type_2 = models.IntegerField('room_price_type_2', null=True)
    room_name = models.CharField('room_name', max_length=50, blank=True)
    image_1=models.ImageField(upload_to='image/',default='Insert Image', null=True)
    # price = models.IntegerField('price')
