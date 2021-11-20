from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import fields
from .models import ProductReview


class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','username','email','password1','password2')

# Review Add Form
class ReviewAdd(forms.ModelForm):
	class Meta:
		model=ProductReview
		fields=('review_text','review_rating')

from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()