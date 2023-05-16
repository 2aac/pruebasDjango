from django.contrib import admin
from .models import Medico, Paciente

# Register your models here.
class MiModelo(admin.ModelAdmin):
    exclude = ('user',)

class MiOtroModelo(admin.ModelAdmin):
    exclude = ('user',)

admin.site.register(Medico, MiModelo)
admin.site.register(Paciente, MiOtroModelo)