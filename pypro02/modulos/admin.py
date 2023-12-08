from django.contrib.admin import register
from ordered_model.admin import OrderedModelAdmin
from pypro02.modulos.models import Modulo


@register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}
