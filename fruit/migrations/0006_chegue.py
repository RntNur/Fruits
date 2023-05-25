# Generated by Django 4.1.5 on 2023-02-19 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0005_order_alter_fruit_supplier_pos_order_order_fruits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chegue',
            fields=[
                ('date_print', models.DateTimeField(auto_now_add=True, verbose_name='Дата распечатки')),
                ('address_print', models.CharField(max_length=150, verbose_name='Место создания чека')),
                ('terminal', models.CharField(max_length=10, verbose_name='Код терминала')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='fruit.order')),
            ],
        ),
    ]
