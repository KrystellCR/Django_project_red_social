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

#Forms lo nombrarmos ProfileForm
#llama a un archivo llamado forms.py
from users.forms import ProfileForm, SignupForm


#loginRquiredMixin es como un @loginrequiered
class UserDetailView(LoginRequiredMixin, DetailView):
	""" User detail View """
	
	template_name='users/detail.html'
	queryset = User.objects.all() #userdetail necesita un queryset apartir de que conjunto de datos va a traer los datos 
	slug_field = 'username' 
	slug_url_kwarg = 'username' #como le llamamos del lado de las urls , es decir    route='<str:username>/',
	context_object_name = 'user' # es el nombre del objeto que vamos a mandar al template
	
	#metodo para agregar datos al contexto /estamos sobreescribiendo este metodo
	#vamos a agregar los posts al usuario
	#mandamos los posts al template ya que los posts pertenecen al modelo posts y no users
	def get_context_data(self, **kwargs):
		"""Add user's posts to context."""
		#traemos el contexto que hubiese traido si no hubiesemos sobreescrito el meotod
		context = super().get_context_data(**kwargs)
		#get_object es el que se encarga de hacer el query del object segun los valores que nosotrs le pasemos
		user = self.get_object()
		#traemos los posts de este usuario user=user
		context['posts'] = Post.objects.filter(user=user).order_by('-created')
		#regresamos el contexto 
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
		
	#EL MODELO QUE VAMOS A UPDETEAR
	model = Profile
	#acepta o el field o el form_class pero no ambas, el form se usa para qeu valide pues de otra manera no lo hace solo usando los fields 
	form_class = ProfileForm
	template_name = 'users/update_profile.html'
	#los fields que va a editar 
	#fields = ['website', 'biography', 'phone_number', 'picture']

	#sobreescribiendo el metodo get_object
	def get_object(self,queryset=None):
		"""Return user's profile."""
		return self.request.user.profile

	#sobreescribiendo el get_success_url para cambiar la url y
	#vamos a details que recibe como parametro un string y se lo agregamos, esto se puede hacer de otra forma pero lo estamos haciendo asi a modo de ejemplo
	#del uso del object.context
	
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



















