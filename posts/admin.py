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
	
	list_display = ('pk','user','title','photo','created','modified')
	list_display_links = ('pk','user')
	list_editable=('title',)
	search_fields = ('title', 'user__username', 'user__email')
	#para filtrar los datos 
	list_filter =(
		'title',
		'created',
		'modified'
	)

	fieldsets = (
        ('Posts',{
            'fields':(('user','user__username','title','photo'),)
        }),
       
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )

	readonly_fields = ('created','modified')
	
	

		