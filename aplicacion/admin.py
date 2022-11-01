from django.contrib import admin
from .models import docente, usuario, coordinador
# Register your models here.

admin.site.register(usuario)
admin.site.register(docente)
admin.site.register(coordinador)