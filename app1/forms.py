from .models import CustomUser
from django import forms


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	# mobile_number = forms.RegexField(regex=r'^\+?1?\d{9,10}$')
	class Meta :
		model = CustomUser
		fields = ['email','password','full_name','mobile_number']
		


# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('email','password','full_name','mobile_number',)

# class CustomUserChangeForm(UserChangeForm):

#     class Meta(UserChangeForm):
#         model = CustomUser
#         fields = ('email','password','full_name','mobile_number',)