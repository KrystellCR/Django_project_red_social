""" USERs Views """

#Django
from django.contrib.auth import authenticate, login, logout # para el login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect #para renderizar
from django.contrib.auth.mixins import LoginRequiredMixin #
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView,FormView,UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

from users.forms import ProfileForm, SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
	""" User detail View """
	
	template_name='users/detail.html'
	queryset = User.objects.all()
	slug_field = 'username' 
	slug_url_kwarg = 'username'
	context_object_name = 'user' 

	def get_context_data(self, **kwargs):
		"""Add user's posts to context."""
		context = super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Post.objects.filter(user=user).order_by('-created')
		return context



class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html' #que template usara 
    form_class = SignupForm #formulario que se usara para validar
    success_url = reverse_lazy('users:login') #a donde te manda si es succesl

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
	"""Update profile view."""
	model = Profile
	form_class = ProfileForm
	template_name = 'users/update_profile.html'


	#sobreescribiendo el metodo get_object
	def get_object(self,queryset=None):
		"""Return user's profile."""
		return self.request.user.profile

	def get_success_url(self):
		"""Return to user's profile."""
		username = self.object.user.username
		return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
	"""Login view."""

	template_name = 'users/login.html'
	redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'



















