from django import forms

from .models import Booking
from .models import Contact

class DateInput(forms.DateInput):
    input_type= 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"
        widgets={
            'booking_date':DateInput(),
        }
        labels={
            'p_name':"Patient Name :",
            'p_phone':"Patient Contact number :",
            'p_email':"patient Email:",
            'doc_name':"Doctor name:",
            'booking_date':"Booking Date :",
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        labels={
            'f_name':"First Name",
            'l_name':"Last Name",
            'pat_phone':"Patient Contact number :",
            'pat_email':"patient Email:",
            'remarks':"Remarks"
        }