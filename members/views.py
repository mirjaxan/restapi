from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 

from .forms import CustumRegisterForm

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user  = authenticate(request,  username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else: 
			messages.success(request, ("Username Or Password is wrong"))
			return redirect('login')
	else:
			return render(request, 'auth/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, 'Siz Hisobdan chiqdingiz!')
	return redirect('home')

def regiser_user(request):
	if request.method == "POST":
		form = CustumRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else: 
		form = CustumRegisterForm()

	return render(request, 'auth/register.html', {"form": form})	
