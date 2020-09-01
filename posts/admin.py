from django.contrib import admin

# Register your models here.


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from posts.models import Post


#models
from users.models import Profile
from django.contrib.auth.models import User
#para editar el Admin/profile
@admin.register(Post)
class Post(admin.ModelAdmin):
	
	#para que aparezcan los atributos de profile en la lista 
	list_display = ('pk','user','title','photo','created','modified')
	#para que aparezcan en forma de links 
	list_display_links = ('pk','user')
	#para editar no pueden ser editables y links al mismo tiempo
	list_editable=('title',)
	#para buscar usamos la relacion de user y sus atributos del modelo user email,...
	search_fields = ('title', 'user__username', 'user__email')
	#para filtrar los datos 
	list_filter =(
		'title',
		'created',
		'modified'
	)
	#tupla con otras tuplas adentro 
	#estas tuplas seccionan los datos en la pagina detalle que se puedan agrupar  
	#cambia el /admin/users/profile/1/change/
	fieldsets = (
        ('Posts',{
            'fields':(('user','user__username','title','photo'),)
        }),
       
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )

	#para que no se editen en detalle ... estos campos no son editables
	#si no los pones readonly sale error 
	readonly_fields = ('created','modified')
	
	

		