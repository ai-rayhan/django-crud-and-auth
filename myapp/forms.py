# forms.py
from django import forms
from .models import Product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model  # Import the get_user_model function

User = get_user_model()  # Get the user model dynamically

class SignUpForm(UserCreationForm):
    # Add additional fields if needed
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price','color']

