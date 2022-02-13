# Generated by Django 4.0.2 on 2022-02-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids_food_management_app', '0002_alter_kid_age_alter_kid_name_alter_kid_parents_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='approved_by',
            field=models.CharField(max_length=299),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_group',
            field=models.CharField(choices=[('Veg', 'Veg'), ('Fruit', 'Fruit'), ('Protein', 'Protein'), ('Dairy', 'Dairy'), ('Confectionery', 'Confectionery'), ('Unknown', 'Unknown')], max_length=15),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.CharField(max_length=9999),
        ),
    ]