from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import re

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','email','password1','password2',]

#     def __init__(self,*args,**kwargs):
#         super(UserCreationForm,self).__init__(*args,**kwargs)

#         for fieldName in ['username','password1','password2']:
#             self.fields[fieldName].help_text=None




class CS_RegisterForm(forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','confirm_password']

    def clean_password1(self):
        password1=self.cleaned_data.get('password1')
        if(len(password1)<8):
            raise forms.ValidationError('Password Must be 8 Character Long!')
        elif not re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", password1):
            raise forms.ValidationError('Password must be include uppercase Lowercase digit and Special character')
        



