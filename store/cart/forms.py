from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone_no = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    state = forms.CharField(max_length=200)
    district = forms.CharField(max_length=200)
    block = forms.CharField(max_length=200)
    post_office = forms.CharField(max_length=255)
    pincode = forms.CharField(max_length=255)
    landmark = forms.CharField(max_length=100)
    place = forms.CharField(max_length=255)