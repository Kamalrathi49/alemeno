# Generated by Django 4.0.2 on 2022-02-15 15:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kids_food_management_app', '0003_alter_food_approved_by_alter_food_food_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='approved_by',
            field=models.CharField(blank=True, max_length=299, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_group',
            field=models.CharField(blank=True, choices=[('Veg', 'Veg'), ('Fruit', 'Fruit'), ('Protein', 'Protein'), ('Dairy', 'Dairy'), ('Confectionery', 'Confectionery'), ('Unknown', 'Unknown')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.CharField(blank=True, max_length=9999, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='is_approved',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='kid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kids_food_management_app.kid'),
        ),
        migrations.AlterField(
            model_name='food',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='kid',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kid',
            name='name',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
        migrations.AlterField(
            model_name='kid',
            name='parents_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='kid',
            name='parents_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
