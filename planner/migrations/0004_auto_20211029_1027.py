# Generated by Django 3.2.8 on 2021-10-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_meal_meal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='day',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
