from django.db import models
from django.utils.text import slugify
class Genre(models.TextChoices):
		ACTION = 'action', 'Action'
		ADVENTURE = 'adventure', 'Adventure'
		RPG = 'rpg', 'RPG'
		STRATEGY = 'strategy', 'Strategy'
		SIMULATION = 'simulation', 'Simulation'
		SPORTS = 'sports', 'Sports'
		PUZZLE = 'puzzle', 'Puzzle'
		HORROR = 'horror', 'Horror'
		OTHER = 'other', 'Other'

class Main(models.Model):
	image = models.FileField(upload_to='images/main-image')
	category  = models.CharField(max_length=10, choices=Genre.choices, default=Genre.SIMULATION)
	name = models.CharField(max_length=250)
	discount = models.DecimalField(max_digits=6, decimal_places=2, null= True, blank=True ) 
	price  = models.DecimalField(max_digits=6, decimal_places=2)


class TopCategory(models.Model):
	image = models.FileField(upload_to='images/main-image')
	category  = models.CharField(max_length=100, choices=Genre.choices, default=Genre.SIMULATION)
	name = models.CharField(max_length=250)
	

class GameDetail(models.Model):
	title = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=6, decimal_places=2)  
	old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  
	description = models.TextField()  
	game_id = models.CharField(max_length=50, unique=True) 
	category = models.CharField(max_length=100, choices=Genre.choices, default=Genre.SIMULATION)  
	multi_tags = models.CharField(max_length=200, blank=True)  
	image = models.FileField(upload_to='games/') 
