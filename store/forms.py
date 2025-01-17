from django import forms
from store.models import LoginModel, CheckoutModel

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = '__all__'
        labels = {
            "name": "Name",
            "email": "Email",
            "password": "Password"
        }
        
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckoutModel
        fields = '__all__'
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "address": "Address",
            "email": "Email",
            "phone_number": "Phone Number",
            "card_number": "Card Number",
            "mmyy": "MM/YY",
            "cvv": "CVV"
        }