from django.shortcuts import render,redirect, get_object_or_404
from user.forms import *
from user.models import *
from user.methods import id_generator
from django.contrib.auth.models import User, Group
import pyrebase
from django.contrib import auth
import razorpay
from django.views.decorators.csrf import csrf_exempt
import smtplib



config = {
    "apiKey": "AIzaSyBBRmSKrQileJ8oxy8qoADQLH_nlLu8U14",
    "authDomain": "hotel-booking-9e415.firebaseapp.com",
    "databaseURL": "https://hotel-booking-9e415-default-rtdb.firebaseio.com",
    "projectId": "hotel-booking-9e415",
    "storageBucket": "hotel-booking-9e415.appspot.com",
    "messagingSenderId": "948727124666",
    "appId": "1:948727124666:web:3b344aab7c36174fdda883",
    # measurementId: "G-DBCY5RVV1C"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def home(request,*args):
    return render(request,"user/home.html")

def check(request,*args):
    return render(request,"user/check.html")

def contact(request,*args):
    return render(request,"user/contact.html")

def about(request,*args):
    return render(request,"user/about.html")

# hotel-1
def hotel1(request,*args):
    name = request.POST.get('c_name')
    email = request.POST.get('c_email')
    contact = request.POST.get('c_contact')
    persons = request.POST.get('c_nop')
    check_in = request.POST.get('c_check_in')
    check_out = request.POST.get('c_check_out')
    room_type = request.POST.get('c_rt')

    data = {
        "name":name,
        "email":email,
        "contact":contact,
        "persons":persons,
        "check_in":check_in,
        "check_out":check_out,
        "room_type":room_type,
        }

    database.child('booking').child("hotel1").child("user"+id_generator()).set(data)
    return render(request,"user/hotel1.html")


# hotel - 2
def hotel2(request,*args):
    name = request.POST.get('c_name')
    email = request.POST.get('c_email')
    contact = request.POST.get('c_contact')
    persons = request.POST.get('c_nop')
    check_in = request.POST.get('c_check_in')
    check_out = request.POST.get('c_check_out')
    room_type = request.POST.get('c_rt')

    data = {
        "name":name,
        "email":email,
        "contact":contact,
        "persons":persons,
        "check_in":check_in,
        "check_out":check_out,
        "room_type":room_type,
        }

    database.child('booking').child("hotel2").child("user"+id_generator()).set(data)
    return render(request,"user/hotel2.html")


# Hotel - 3
def hotel3(request,*args):
    name = request.POST.get('c_name')
    email = request.POST.get('c_email')
    contact = request.POST.get('c_contact')
    persons = request.POST.get('c_nop')
    check_in = request.POST.get('c_check_in')
    check_out = request.POST.get('c_check_out')
    room_type = request.POST.get('c_rt')

    data = {
        "name":name,
        "email":email,
        "contact":contact,
        "persons":persons,
        "check_in":check_in,
        "check_out":check_out,
        "room_type":room_type,
        }

    database.child('booking').child("hotel3").child("user"+id_generator()).set(data)
    return render(request,"user/hotel3.html")

# hotel - 4

def hotel4(request,*args):
    return render(request,"user/hotel4.html")


# Check for hotel's room availability

# Hotel1
def check_date1(request,*args):
    date = request.POST.get('check_date')
    global hName
    hName = "MK Hotel And Resort"

    booked_room= []
    user_list = database.child('booking').child('MK Hotel And Resort').get().val()

    for user in user_list:
        if(database.child('booking').child('MK Hotel And Resort').child(user).child("Date").get().val()==str(date)):
            room = int(database.child('booking').child('MK Hotel And Resort').child(user).child("roomno").get().val())
            booked_room.append(room)
    
    available_room = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124]  

    return render(request,"user/check_date1.html",{'booked_room':booked_room,'available_room':available_room, 'date':date})

# Hotel2
def check_date2(request,*args):
    date = request.POST.get('check_date')
    global hName
    hName = "Hotel Royal King"

    booked_room= []
    user_list = database.child('booking').child('Hotel Royal King').get().val()

    for user in user_list:
        if(database.child('booking').child('Hotel Royal King').child(user).child("Date").get().val()==str(date)):
            room = int(database.child('booking').child('Hotel Royal King').child(user).child("roomno").get().val())
            booked_room.append(room)
    
    available_room = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124]  

    return render(request,"user/check_date2.html",{'booked_room':booked_room,'available_room':available_room, 'date':date})

# Hotel3
def check_date3(request,*args):
    date = request.POST.get('check_date')
    global hName
    hName = "Rosewood Resort"

    booked_room= []
    user_list = database.child('booking').child('Rosewood Resort').get().val()

    for user in user_list:
        if(database.child('booking').child('Rosewood Resort').child(user).child("Date").get().val()==str(date)):
            room = int(database.child('booking').child('Rosewood Resort').child(user).child("roomno").get().val())
            booked_room.append(room)
    
    available_room = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124]

    return render(request,"user/check_date3.html",{'booked_room':booked_room,'available_room':available_room, 'date':date})

# Hotel4
def check_date(request,*args):
    date = request.POST.get('check_date')
    global hName
    hName ="Hotel Haunted"

    booked_room= []
    user_list = database.child('booking').child('Hotel Haunted').get().val()

    for user in user_list:
        if(database.child('booking').child('Hotel Haunted').child(user).child("Date").get().val()==str(date)):
            room = int(database.child('booking').child('Hotel Haunted').child(user).child("roomno").get().val())
            booked_room.append(room)
    
    available_room = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124]

    return render(request,"user/check_date.html",{'booked_room':booked_room,'available_room':available_room, 'date':date})

# Check for hotel and resort availability
def check(request,*args):
    date = request.POST.get('date')

    available_hotels =[]
    available_room = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124]

    hotel_list = database.child('booking').get().val()
    for hotel in hotel_list:
        room_list = []
        for user in database.child('booking').child(hotel).get().val():
            if(database.child('booking').child(hotel).child(user).child("Date").get().val()==str(date)):
                room = int(database.child('booking').child(hotel).child(user).child("roomno").get().val())
                room_list.append(room)

        room_list.sort()        
        if(room_list!=available_room):
            avl_room = len(available_room)-len(room_list)
            available_hotels.append([hotel,avl_room])
        print(room_list)
        print(avl_room)
    
    print(available_hotels)
    print(date)

    return render(request,"user/check.html",{"available_hotels": available_hotels,"date":date})

# Register
def register(request,*args):
    if request.method == "POST": 
        form = hotelReg(request.POST or None)
        if form.is_valid():
            details = form.cleaned_data
            new_hotelName = details['hotelName']
            new_typeName = details['typeName']
            new_email = details['email']
            new_hotel_url  = details['hotel_url']
            new_hotel_id = id_generator()

            print(new_hotelName,new_typeName,new_email)

            newhotel = hotel(
                        hotelName = str(new_hotelName),
                        typeName = str(new_typeName),
                        email = str(new_email.lower()),
                        hotel_url = str(new_hotel_url),
                        hotel_id = str(new_hotel_id)
                        # isActive=False
                        )
            newUser = User.objects.create_user(
                        username=str(new_hotelName.lower()),
                        email=str(new_email.lower()),
            )
            
            newhotel.save()
            newUser.save()
            
            return redirect("../user/home")
    else:
        form = hotelReg(request.POST or None)
        for field in form.errors:
                form[field].field.widget.attrs['class'] += 'error'
        
    return render(request,"user/register.html",{"form":form})

# payment details
def payhome(request, *args):
    if request.method == "POST":
        global room_type
        if request.POST.get('c_rt') == '1':
            room_type = "Luxuries Room"
            room_price = "150000"
        elif request.POST.get('c_rt') == '2':
            room_type = "Deluxe Room"
            room_price = "100000"
        elif request.POST.get('c_rt') == '3':    
            room_type = "Signature Room"
            room_price = "200000"
        elif request.POST.get('c_rt') == '4':
            room_type = "Couple Room"
            room_price = "250000"

        amount = int(room_price)
        currency= 'INR',
        

        print(request.POST.get('room_type'))

        client = razorpay.Client(auth=("rzp_test_YRyLn9WVhONbmD", "PgNbmGkK39o0SyBQ7kWiYRWe"))
        payment = client.order.create({'amount':amount,'currency': 'INR','payment_capture': '1'})


        # Save User Details
        name = request.POST.get('c_name')
        email = request.POST.get('c_email')
        contact = request.POST.get('c_contact')
        persons = request.POST.get('c_nop')
        Date = request.POST.get('c_check_in')
        room_no = request.POST.get('c_room_no')
        room_type = request.POST.get('c_rt')

        global data 
        data = {
            "name":name,
            "email":email,
            "contact":contact,
            "persons":persons,
            "Date":Date,
            "roomno":room_no,
            "room_type":room_type,
            }
       

    return render(request, 'user/payment.html',{'name':name,"email":email,"contact":contact,"persons":persons,"Date":Date,"roomno":room_no,"room_type":room_type,'room_price':room_price,"hName":hName})

@csrf_exempt
def success(request):
    userId = "user"+id_generator()
    database.child('booking').child(hName).child(userId).set(data)

    smtpob = smtplib.SMTP('smtp.gmail.com', 587)
    smtpob.starttls()
    smtpob.login("mvatsfoundation@gmail.com","Bangbang0!")
    recv=data['email']
    subject= "Booking Details"
    Thanks="Dear "+ data['name']+"\n\nThanks for booking with us. \nYour Booking Details are as follows: \n"
    detail= "Booking Id: "+ userId+"\nRoom No.: "+data['roomno']+"\nRoom Type: "+ data['room_type']+"\nHotel Name: "+hName+"\nDate: "+data['Date']
    bill="Your bill is Rs. "+str(2500)+"/-"
    message ="Subject :{}\n{}{}\n{}\n\n\n Best Regards \n Unite.com".format(subject,Thanks,detail,bill)
    smtpob.sendmail('mvatsfoundation@gmail.com',recv, message)
    smtpob.quit()

    return render(request, "user/success.html")
   
#  Cancel Booking
def cancel(request,*args):
    if request.method == "POST":
            booking_id = request.POST.get('booking_id')
            hotel_name = request.POST.get('hotel_name')
            

            # Fectched Booking Details
            booking_details = database.child('booking').child(hotel_name).child(booking_id).get()

            # error handling
            if booking_details.val() == None:
                return render(request,"user/cancel.html",{"error":1})
            else:
                
                email = booking_details.val()['email']
                name = booking_details.val()['name']

                database.child('booking').child(hotel_name).child(booking_id).remove()
                # Cancelation Mail
                smtpob = smtplib.SMTP('smtp.gmail.com', 587)
                smtpob.starttls()
                smtpob.login("mvatsfoundation@gmail.com","Bangbang0!")
                recv = email
                subject = " Booking Cancellation"
                Thanks="Dear "+name +"\n \nYour Booking has been cancelled successfully. \n"
                bill="Your refunded amount will be send to your account in 5 working days."
                message ="Subject :{}\n{}{}\n\n Best Regards \n Unite.com".format(subject,Thanks,bill)
                smtpob.sendmail('mvatsfoundation@gmail.com',recv, message)
                smtpob.quit()

                return render(request,"user/cancel.html",{"error":2})
    return render(request,"user/cancel.html")   
