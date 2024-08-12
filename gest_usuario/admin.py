from django.contrib import admin

# Register your models here.
from .models import Jugadores, Chats, Statistics

@admin.register(Jugadores)
class PostAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'nombre', 'apellidos')
admin.site.register(Chats)
admin.site.register(Statistics)