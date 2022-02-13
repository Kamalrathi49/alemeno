from unicodedata import name
from django.urls import path
from kids_food_management_app import views

urlpatterns = [
    path('', views.KidsList, name='home'),
    path('addkid/', views.AddKid, name='add-kid'),
    path('editkid/<int:kid_pk>', views.EditKidProfile, name='edit-kid'),
    path('deletekid/<int:kid_pk>', views.delete_KidProfile, name='delete-kid'),
    path('foods/<int:kid_pk>', views.FoodList, name='display-food'),
    path('addfood/<int:kid_pk>', views.addFood, name='add-food'),
    path('editfood/<int:kid_pk>/<int:food_pk>', views.EditFood, name='edit-food'),
    path('deletefood/<int:food_pk>/<int:kid_pk>', views.delete_Food, name='delete-food'),
]