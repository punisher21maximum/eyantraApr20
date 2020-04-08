from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']


#update forms
#registration
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


#profile
from .models import Profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
#update
#person
from .models import Person
class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['user']

#shop
from .models import Shop
class ShopUpdateForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ['user']

#create
#person
# from .models import Person
class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['user']

#shop
# from .models import Shop
class ShopcreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ['user']


