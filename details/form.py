from django import forms
from django.core import validators
from .models import User

class registration(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['name','lastname','username', 'email', 'password','cpassword', 'address']
        labels = {
            "name" :"First Name",
            "lastname" : "Last Name",
            "username" : "Username",
            "email" :"Email",
            "password" :"Password",
            "cpassword" :"Confirm Password",
            "address" :"Address",            
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control'}),
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value = True, attrs={'class': 'form-control'}),
            'cpassword' : forms.PasswordInput(render_value = True, attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
        }




    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password",None)
        confirm_password = cleaned_data.get("cpassword",None)

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )