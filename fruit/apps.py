from django.apps import AppConfig


class FruitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fruit'
    # Название приложения для отображения
    verbose_name='Магазин фруктов'
