
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

class PostDetailView(LoginRequiredMixin, DetailView):
	""" User detail View """
	
	template_name='posts/post_detail.html'
	queryset = Post.objects.all() 
	slug_field = 'id' 
	slug_url_kwarg = 'post_id' 
	context_object_name = 'post' 

	
class CreatePostView(LoginRequiredMixin, CreateView):
	"""Create a new post."""

	template_name = 'posts/new.html'
	form_class = PostForm 
	success_url = reverse_lazy('posts:feed')


	def get_context_data(self, **kwargs):
		"""Add user and profile to context."""
		context = super().get_context_data(**kwargs) 
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		context['test'] = 'exitoooo'
		return context
		
		
		

	
