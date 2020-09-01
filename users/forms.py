"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.postgres.forms import SimpleArrayField

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    #se usa un widget
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput() 
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
	
	#CUANDO QUIERES VALIDAR UN CAMPO APARTE USAS LA FUNCION CLEAN_FIELD
    def clean_username(self):
        """Username must be unique."""
		
		#toma el dato de 'username'
        username = self.cleaned_data['username']
		#checa si en la tabla ya existe el usuario 
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
			#si existe lanzamos una excepcion
            raise forms.ValidationError('Username is already in use.')
		#SIEMPRE SE DEBE DE REGRESAR EL VALOR CUANDO ESTAS USANDO UNA VALIDACION
		#SI NO HAY ERROR REGRESAS EL USERNAME
        return username

	#para validar un campo que depende de otro 
    def clean(self):
        """Verify password confirmation match."""
			
		#super una forma de llamar a clean antes de ser sobre escrito
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

		#COPIA TODO EL DICCIONARIO CON **dATA
		#**D
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.ModelForm):
  website = forms.URLField(max_length=200,required=False)
  biography = forms.CharField(max_length=500,required=True)
  phone_number = forms.CharField(max_length=20,required=False)
  picture = forms.ImageField(required=True)

  class Meta:
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

	
	