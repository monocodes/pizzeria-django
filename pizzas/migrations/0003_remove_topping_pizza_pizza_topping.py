# Generated by Django 4.1.4 on 2022-12-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='pizza',
        ),
        migrations.AddField(
            model_name='pizza',
            name='topping',
            field=models.ManyToManyField(blank=True, to='pizzas.topping'),
        ),
    ]