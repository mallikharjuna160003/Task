from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm,widgets
from .models import Profile,Address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
    
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'