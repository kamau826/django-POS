from django.forms import ModelForm
from . models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddProduct(ModelForm):
	class Meta:
		model=Product
		fields='__all__'
class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']
