
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #
from django.views.generic import DetailView,CreateView,ListView
from django.http import HttpResponse 

from posts.forms import PostForm

#utilities
from datetime import datetime
# importar el modelo
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
	""" REturn all published posts """
	
	template_name = 'posts/feed.html' 
	model = Post
	ordering = ('-created',)
	paginate_by = 2
	context_object_name = 'posts'
	
#loginRquiredMixin es como un @loginrequiered
class PostDetailView(LoginRequiredMixin, DetailView):
	""" User detail View """
	
	template_name='posts/post_detail.html'
	queryset = Post.objects.all() #userdetail necesita un queryset apartir de que conjunto de datos va a traer los datos 
	slug_field = 'id' 
	slug_url_kwarg = 'post_id' #como le llamamos del lado de las urls , es decir    route='<str:username>/',
	context_object_name = 'post' # es el nombre del objeto que vamos a mandar al template


	
class CreatePostView(LoginRequiredMixin, CreateView):
	"""Create a new post."""

	template_name = 'posts/new.html'
	form_class = PostForm #EL FORMURLARIO QEU SE USARA PARA VALIDAR 
	success_url = reverse_lazy('posts:feed') #VA A BUSCAR LA URL

	#SOBRE ESCRIBIMOS EL METODO GET_CONTEXT_DATA
	def get_context_data(self, **kwargs):
		"""Add user and profile to context."""
		#EL CONTEXTO SERA EL QUE HUBIESE TRAIDO SI NO SOBREESCRIBIMOS LA CLASE
		context = super().get_context_data(**kwargs) 
		#AGREGAMOS AL CONTEXTO EL USER Y EL PROFILE
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		context['test'] = 'exitoooo'
		return context
		
		
		

	
