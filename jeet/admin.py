from django.contrib import admin
from .models import ContactMessage,BlogPost,Project

# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(BlogPost)
admin.site.register(Project)

