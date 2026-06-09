from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import re
from tasks.forms import StyleMixin

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','email','password1','password2',]

#     def __init__(self,*args,**kwargs):
#         super(UserCreationForm,self).__init__(*args,**kwargs)

#         for fieldName in ['username','password1','password2']:
#             self.fields[fieldName].help_text=None




class CS_RegisterForm(StyleMixin,forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','confirm_password']

    def clean_password1(self):
        password1=self.cleaned_data.get('password1')

        errors = []
        if len(password1) < 8:
            errors.append('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password1):
            errors.append('Password must include at least one uppercase letter.')
        if not re.search(r'[a-z]', password1):
            errors.append('Password must include at least one lowercase letter.')
        if not re.search(r'[0-9]', password1):
            errors.append('Password must include at least one number.')
        if not re.search(r'[@#$%^&+=]', password1):
            errors.append('Password must include at least one special character.')
        if errors:
            raise forms.ValidationError(errors)
        return password1
    

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if(User.objects.filter(email=email)).exists():
            raise forms.ValidationError('Email Already Exist')
        return email

    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get('password1')
        confirm_password=cleaned_data.get('confirm_password')
        
        if password1 and confirm_password and password1 != confirm_password:
            raise forms.ValidationError("Both Password Must Be Same")
        return cleaned_data
    




        



