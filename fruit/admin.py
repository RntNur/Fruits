from django.contrib import admin
from .models import Fruit, Supplier, Order, Pos_order, Chegue


class FruitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'supplier', 'exist')  # Отображение полей
    list_display_links = ('id', 'name')  # Установка ссылок на атрибуты
    search_fields = ('name', 'price')  # Поиск по полям
    list_editable = ('price', 'exist')  # Изменяемое поле
    list_filter = ('exist', 'supplier')  # Фильтры полей


admin.site.register(Fruit, FruitAdmin)  # (Модель, Форма Админки модели)


# Название атрибутов в модели, прописывается в самих атрибутах (models)
# Название модели и сортировка её атрибутов прописывается в классе Meta (models)
# Отображение моделей на админки прописывается в классе ModelAdmin (admin)
# Название приложения прописывается в настройках приложения (apps)


# Supplier
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'agent_firstname', 'agent_name', 'agent_patronymic', 'exist')  # Отображение полей
    list_display_links = ('id', 'title')  # Установка ссылок на атрибуты
    search_fields = ('title', 'agent_firstname')  # Поиск по полям
    list_editable = ('exist',)  # Изменяемое поле
    list_filter = ('exist',)  # Фильтры полей


admin.site.register(Supplier, SupplierAdmin)


# Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_create', 'date_finish', 'status', 'price', 'address_delivery')  # Отображение полей
    list_display_links = ('id',)  # Установка ссылок на атрибуты
    search_fields = ('date_create', 'address_delivery')  # Поиск по полям
    list_editable = ('date_finish', 'status')  # Изменяемое поле
    list_filter = ('status',)  # Фильтры полей


admin.site.register(Order, OrderAdmin)


# Position order
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('id', 'fruit', 'order', 'count_fruit', 'price')  # Отображение полей
    list_display_links = ('fruit', 'order')  # Установка ссылок на атрибуты
    search_fields = ('fruit', 'order')  # Поиск по полям


admin.site.register(Pos_order, Pos_orderAdmin)


# Cheque
class ChequeAdmin(admin.ModelAdmin):
    list_display = ('order', 'date_print', 'address_print', 'terminal')  # Отображение полей
    list_display_links = ('order', 'date_print')  # Установка ссылок на атрибуты
    search_fields = ('date_print', 'address_print')  # Поиск по полям


admin.site.register(Chegue, ChequeAdmin)
