"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
	"""Profile completion middleware. Ensure every user that is interacting with the platform have their profile picture and biography."""
	def __init__(self, get_response):
		"""Middleware initialization."""
		#trae response 
		self.get_response = get_response


	def __call__(self, request):
		"""Code to be executed for each request before the view is called."""
        #verificamos que halla un usuario logueado 
		if not request.user.is_anonymous:
			if not request.user.is_staff:
				#traemos el perfil esto es una manera de traer los one to one field
				profile = request.user.profile
				#si no tiene picture o no tiene biografia 
				if not profile.picture or not profile.biography:
					#si tu url no es users:update o logout entonces te regresa a update 
					if request.path not in [reverse('users:update'), reverse('users:logout')]:
						return redirect('users:update')


		#en caso de que no caiga en los ifs regresamos la respuesta tal y como esta
		response = self.get_response(request)
		return response