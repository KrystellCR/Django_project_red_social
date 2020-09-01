from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from users.models import Profile

#para editar el Admin/profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	
	#para que aparezcan los atributos de profile en la lista 
	list_display = ('pk','user','phone_number','website','picture')
	#para que aparezcan en forma de links 
	list_display_links = ('pk','user')
	#para editar no pueden ser editables y links al mismo tiempo
	list_editable=('phone_number','website','picture')
	#para buscar usamos la relacion de user y sus atributos del modelo user email,...
	search_fields=(
		'user__username',
		'user__email',
		'user__first_name',
		'user__last_name'
	)
	#para filtrar los datos 
	list_filter =(
		'created',
		'modified',
		'user__is_active',
		'user__is_staff'
	)
	#tupla con otras tuplas adentro 
	#estas tuplas seccionan los datos en la pagina detalle que se puedan agrupar  
	#cambia el /admin/users/profile/1/change/
	fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography'),
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )

	#para que no se editen en detalle ... estos campos no son editables
	#si no los pones readonly sale error 
	readonly_fields = ('created','modified')
	
	
#esto es para crear un usuario con su profile al mismo tiempo 	
class ProfileInLine(admin.StackedInline):
		model = Profile
		can_delete = False
		verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
		inlines = (ProfileInLine,)
		list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
		
	
#desregistras el admin que ya existe para que n ose muestre igual		
admin.site.unregister(User)
#registras el nuevo UserAdmin
admin.site.register(User,UserAdmin)

		