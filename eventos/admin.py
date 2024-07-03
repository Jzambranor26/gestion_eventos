from django.contrib import admin
from .models import Usuario, Evento, Inscripcion


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'is_admin')
    search_fields = ('email', 'nombre')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'fecha', 'hora', 'creador']
    search_fields = ['nombre', 'descripcion', 'ubicacion']
    list_filter = ['fecha', 'hora', 'creador']


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('evento', 'usuario', 'fecha_inscripcion')
    search_fields = ('evento__nombre', 'usuario__nombre')
    readonly_fields = ('id',)
