from django.contrib import admin
from .models import Main, TopCategory, GameDetail

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')
	list_filter = ('category', )
	search_fields = ('name', )

@admin.register(TopCategory)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')


@admin.register(GameDetail)
class DetailAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'category')
	list_filter  = ('price', 'category')
	search_fields = ('description', 'game_id')