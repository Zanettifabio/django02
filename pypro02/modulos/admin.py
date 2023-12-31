from django.contrib.admin import register
from ordered_model.admin import OrderedModelAdmin
from pypro02.modulos.models import Modulo, Aula


@register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'order', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}


@register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'order', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}
    list_filter = ('modulo',)
    ordering = ('modulo', 'order')
