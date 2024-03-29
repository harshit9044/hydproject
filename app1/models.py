from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
# Create your models here.

# class MyUser(models.Model):

# 	user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	mobile_number = models.BigIntegerField(null=False,blank=False,max_length=10)
# 	full_name     = models.CharField(null=False,blank=False,max_length=290)
# 	email         = models.CharField(null=False,blank=False,max_length=100)


class Extras(models.Model):
	location = models.CharField(max_length=100)
	language = models.CharField(max_length=75)



class CustomUserManager(BaseUserManager):

	def create_user(self,email,mobile_number,full_name,password=None):
		if not email:
			raise ValueError("User must have email")

		if not mobile_number:
			raise ValueError("User must have mobile number")

		if not full_name:
			raise ValueError("User must have full name")

		user = self.model(
				email=self.normalize_email(email),
				mobile_number=mobile_number,
				full_name=full_name,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,mobile_number,full_name,password):
		user  = self.create_user(
				email=self.normalize_email(email),
				mobile_number=mobile_number,
				full_name=full_name,
				password=password,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class CustomUser(AbstractBaseUser):

	email         = models.EmailField(verbose_name="email",max_length=60,unique=True)
	mobile_number = models.BigIntegerField(null=False,blank=False)
	full_name     = models.CharField(null=False,blank=False,max_length=290)

	date_joined   = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
	last_login    = models.DateTimeField(verbose_name='last login',auto_now=True)
	is_admin      = models.BooleanField(default=False)
	is_active     = models.BooleanField(default=True)
	is_staff      = models.BooleanField(default=False)
	is_superuser  = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['mobile_number','full_name']

	objects = CustomUserManager()

	def __str__(self):
		return self.email

	def has_perm(self,perm , obj=None):
		return self.is_admin

	def has_module_perms(self , app_label):
		return True

