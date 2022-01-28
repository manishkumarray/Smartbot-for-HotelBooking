from user.models import *
import datetime
import random
import string

def id_generator():
    today = datetime.datetime.now()
    year = str(today.year)
    year = year[2:]
    while True:
        new_hotel_id = ''.join([str(random.choice(string.digits)) for n in range(8)])
        new_hotel_id = year + new_hotel_id
        if hotel.objects.filter(hotel_id=new_hotel_id).exists():
            pass
        else:
            break
    
    return new_hotel_id