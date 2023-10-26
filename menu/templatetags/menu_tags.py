from django import template
from django.urls import reverse
from menu.models import Menu

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    # Получаем меню по названию
    menu = Menu.objects.filter(name=menu_name).prefetch_related('menuitem_set').first()

    # Еслю меню не найдено => пустой контекст
    if not menu:
        return {}
    
    # Получаем все пункты меню для данного меню
    menu_items = menu.menuitem_set.all() if menu else []

    # Добавляем меню и его пункты в контекст
    context['menu_name'] = menu_name
    context['menu_items'] = menu_items

    return context