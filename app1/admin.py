from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Extras
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Extras)



# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email','full_name','mobile_number']

# admin.site.register(CustomUser, CustomUserAdmin)