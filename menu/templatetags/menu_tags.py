from django import template
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

    # По какой то неведомой мне причине, логика работы выбора активного пункта меню не работает, 
    # было бы круто, если бы вы сказали почему))
    
    # current_url = context.get('current_url')

    # active_item = None
    # for item in menu_items:
    #     if current_url == item.url:
    #         active_item = item
    #         break

    # Добавляем меню и его пункты в контекст
    context['menu_name'] = menu_name
    context['menu_items'] = menu_items
    # context['active_item'] = active_item

    return context