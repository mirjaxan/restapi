from django.urls import path 
from .views import Home,ShopView, ProductDetailView, ContactView


urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('shop/', ShopView.as_view(), name='shop'),
	path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
	path('contact/', ContactView.as_view(), name='contact')
]