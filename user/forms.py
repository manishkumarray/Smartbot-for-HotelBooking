from django import forms
from user.models import hotel
import re


class hotelReg(forms.ModelForm):
    type_choices = hotel.type_choices

    hotelName = forms.CharField(label="",required=True,
                widget=forms.TextInput(attrs={"placeholder":"Hotel name",
                                             "size":"40",
                                            "class":"text"}))
                                            
    typeName = forms.ChoiceField(label='',choices=type_choices,
                          widget=forms.Select(attrs={
                              "class":"Choice1"})) 
    
    email = forms.EmailField(label="",required=True,
                widget=forms.TextInput(attrs={"placeholder":"Email Id",
                                             "size":"40",
                                            "class":"text"}))

    hotel_url = forms.CharField(label="",required=True,
                widget=forms.TextInput(attrs={"placeholder":"Hotel Url",
                                             "size":"40",
                                            "class":"text"}))

    class Meta:
        model = hotel
        fields= [
            'hotelName',
            'typeName',
            'email',
            'hotel_url',]

    def clean(self,*args,**kwargs):
        cleaned_data = super().clean()
        email = str(self.cleaned_data.get("email"))

        # validates email
        try:
            email_not_valid = False
            if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
                email_error = "Not a valid email"
                email_not_valid = True
                raise forms.ValidationError(email_error)
        except forms.ValidationError as e:
            self.add_error('email', e)
        