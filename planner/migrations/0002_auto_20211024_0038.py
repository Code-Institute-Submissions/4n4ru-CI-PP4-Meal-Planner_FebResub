# Generated by Django 3.2.8 on 2021-10-24 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meals',
            new_name='Meal',
        ),
        migrations.RenameModel(
            old_name='MealTypes',
            new_name='MealType',
        ),
    ]
