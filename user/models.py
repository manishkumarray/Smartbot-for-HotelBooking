from django.db import models

# Create your models here.
class hotel(models.Model):
    type_choices=(('Hotel','Hotel'),
                    ('Resort','Resort'),
                    ('Villa','Villa'),
                    ('Farm House','Farm House'))

    hotelName = models.CharField(max_length=70,
                     default='',
                    verbose_name="Hotel Name")

    typeName = models.CharField(max_length=70,
                    default='',
                    verbose_name="Type Name",
                    choices=type_choices)
            
    hotel_id = models.CharField(max_length=20,
                verbose_name="Hotel Id",default='',primary_key=True)

    email = models.EmailField(max_length=70,
                    verbose_name="Email")
    
    hotel_url = models.CharField(max_length=50,
                        verbose_name="Hotel Url")


    