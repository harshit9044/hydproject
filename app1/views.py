from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .models import Extras



# Create your views here.
@login_required(login_url='/login/')
def homeview(request):
	myuser = request.user

	all_extras = Extras.objects.all()
	ll = len(all_extras)

	return render(request,'home.html',{
		'full_name':myuser.full_name,
		'email':myuser.email,
		'mobile_number':myuser.mobile_number,
		'extras':all_extras,
		'length':ll,
		})


class UserFormView(View):
	form_class = UserForm
	template_name = 'register.html'


	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			full_name = form.cleaned_data['full_name']
			mm = form.cleaned_data['mobile_number']

			c = int(mm/1000000000)

			if 0<c<=9:
				mobile_number=mm
			else :
				return HttpResponse("<h3>Enter Valid 10 digit mobile number .</h3>")

 
			user.set_password(password)
			user.save()
			# return render(request,'login.html',{})
			return redirect('/login/')

		else :
			return HttpResponse("<h1>INVALID FORM</h1>")


def userloginview(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)

		if user is not None:

			if user.is_active :
				login(request,user)
				# return render(request,'homepage.html',{})
				# return render(request,'home.html',{})
				return redirect('/')

			else :
				return HttpResponse("Your Account has been deactivated")
		else :
			return HttpResponse("Invalid Login Details : ",username,password)

	else :
		return render(request,'login.html',{})


def userlogoutview(request):

	logout(request)
	return redirect('/login/')






