from django.db import models
from django.contrib.auth.models import User #importamos contrib.auth

# Create your models here.

class Profile(models.Model):
	"""Profile model 
		proxy model that extends the base data with other information"""
		
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	website = models.URLField(max_length=200,blank=True)
	biography = models.TextField(blank=True)
	phone_number = models.CharField(max_length=20,blank=True)
	
	#jango no guarda imagenes , solo guarda referencias de la imagen
	picture = models.ImageField(
		upload_to='users/pictures',
		blank=True,
		null=True
		)
		
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	#para regresar un string en lugar de un object con id cuando estamso en la cosola
	
	def __str__(self):
		"""return a string username """
		#user porque username esta en user no en profile y estamos usando un proxy
		return self.user.username
		


