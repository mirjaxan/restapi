from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from datetime import datetime

from .models import Main, GameDetail, TopCategory
from .forms import UserForm

class Home(LoginRequiredMixin,ListView):
	model = Main
	login_url = '/members/login_user'
	redirect_field_name = 'next'
	context_object_name = 'mainProduct'
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
				context = super().get_context_data(**kwargs)
				context['mainProduct'] = Main.objects.all()
				context['topCategory'] = TopCategory.objects.all()
				return context

class ShopView(ListView):
	template_name = 'shop.html'
	model = Main
	context_object_name = 'shops'
	paginate_by = 2


	def get_context_data(self, **kwargs):
		context =  super().get_context_data(**kwargs)
		context['current_year'] = datetime.now().year 
		return context

class ProductDetailView(DetailView):
	template_name = 'product-details.html'
	model = GameDetail
	context_object_name = 'product'

class ContactView(ListView):
	template_name = 'contact.html'
	model = Main



