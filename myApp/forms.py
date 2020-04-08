from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Owner_model


#extend User model
'''
This is how we extend the inbuit 'User' model, to add more fields.
User (inbuilt model) has only 1]username 2]password1 3]password2
Here adding field --> 4]email
from django.core.validators import RegexValidator

class PhoneModel(models.Model):
    ...
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
'''
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, min_length=3)#x1
    last_name = forms.CharField(max_length=30, min_length=3)#x2
    email = forms.EmailField() 
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
        max_length=10, blank=True) # validators should be a list
    adhaar_regex = RegexValidator(regex=r'^\d{4}\s\d{4}\s\d{4}$', 
        message="eg. 1234 1234 1234")
    adhaar_no = forms.CharField(max_length=30, min_length=3)#x3
    image = forms.ImageField(default='default.jpg', upload_to='user_pics')
    class Meta:
        model = User
        # fields = ['username', 'email', 'phone_number',
        # 'password1', 'password2']

        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number',
        'adhaar_no', 'image', 'password1', 'password2']



#update User info
'''
Update User info 
(like username or email ; password is not allowed to be changed by using a form)
'''
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, min_length=3)#x1
    last_name = forms.CharField(max_length=30, min_length=3)#x2
    email = forms.EmailField() 
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
        max_length=10, blank=True) # validators should be a list
    adhaar_regex = RegexValidator(regex=r'^\d{4}\s\d{4}\s\d{4}$', 
        message="eg. 1234 1234 1234")
    adhaar_no = forms.CharField(max_length=30, min_length=3)#x3
    image = forms.ImageField(default='default.jpg', upload_to='user_pics')

    class Meta:
        model = User
        # fields = ['username', 'email']
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number',
        'adhaar_no', 'image']

#update Profile info`ty      

'''
Update Profile info
(like dp)'''

# class Owner_modelUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Owner_model
#         exclude = ['user']





'''
#prev
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Owner_model


#extend User model
'''
# This is how we extend the inbuit 'User' model, to add more fields.
# User (inbuilt model) has only 1]username 2]password1 3]password2
# Here adding field --> 4]email
# from django.core.validators import RegexValidator

# class PhoneModel(models.Model):
#     ...
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
'''
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
        max_length=10, blank=True) # validators should be a list


    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number',
        'password1', 'password2']



#update User info
'''
# Update User info 
# (like username or email ; password is not allowed to be changed by using a form)
'''
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#update Profile info`ty      

'''
# Update Profile info
# (like dp)
'''

class Owner_modelUpdateForm(forms.ModelForm):
    class Meta:
        model = Owner_model
        exclude = ['user']


'''




