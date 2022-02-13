from django.http import HttpResponse
from django.shortcuts import redirect, render
from kids_food_management_app.forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

def KidsList(request):
    kids = Kid.objects.all()
    addkidform = addKidForm()
    ctx = {'kids':kids, 'addkidform':addkidform}
    return render(request, 'index.html', ctx)
    
def FoodList(request, kid_pk):
    foods = Food.objects.filter(kid__pk=kid_pk)
    kid = Kid.objects.get(id=kid_pk)
    addfoodform = addFoodForm()
    ctx = {'foods':foods, 'addfoodform':addfoodform, 'kid': kid}
    return render(request, 'display_food.html', ctx)

def AddKid(request):
    if request.method == 'POST':
        form = addKidForm(request.POST)
        if form.is_valid():
            kid = form.save()
            messages.success(request, f"Kid's profile created Successfully!")
            return redirect('/')
        else:
            messages.error(request, f"Something went wrong, Please try again!")
            return redirect('/')
    else:
        form = addKidForm
        ctx = {'addkidform':form}
        return render(request, 'add_kidsprofile.html', ctx)

    

def EditKidProfile(request, kid_pk):
    if request.method == 'POST':
        kid = Kid.objects.get(pk=kid_pk)
        form = addKidForm(request.POST or None, instance = kid)
        if form.is_valid():
            form.save()
            messages.success(request, f"Kid's profile updated successfully!")
            return redirect('/')
        else: 
            messages.error(request, f"Something went wrong, Please try again!")
            return redirect('/')
    else:
        kid = Kid.objects.get(pk=kid_pk)
        form = addKidForm(request.POST or None, instance = kid)
        ctx = {'editkidsform': form, 'kid': kid}
        return render(request, 'edit_kidsprofile.html', ctx)

def delete_KidProfile(request, kid_pk):
    Kid.objects.get(pk=kid_pk).delete()
    messages.success(request, f"Kid's profile deleted seccessfully!" )
    return redirect('/')

def addFood(request, kid_pk):
    if request.method == 'POST':
        kid = Kid.objects.get(pk=kid_pk)
        form = addFoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.kid = kid
            food.save()
            if food.food_group == 'Unknown':
                subject = f"Image does not contains Food"
                message = f"Hello , \nthis is to inform you that your child {food.kid.name}'s food image does not conatain any food  \nThank You"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [kid.parents_email,]
                send_mail( subject, message, email_from, recipient_list )
                print('--------------email sent-----------')
            else:
                print('--------fail---------')
            messages.success(request, f"Food added Successfully!")
            return redirect(f"/foods/{kid.id}")
        else:
            messages.error(request, f"Email not sent, please try again later!")
            return redirect(f"/foods/{kid.id}")
    else:
        form = addFoodForm
        ctx = {'addfoodform': form}
        return render(request, 'addfood.html', ctx)

def EditFood(request, kid_pk, food_pk):
    if request.method == 'POST':
        kid = Kid.objects.get(pk=kid_pk)
        food = Food.objects.get(pk=food_pk)
        form = addFoodForm(request.POST or None, instance = food)
        if form.is_valid():
            food = form.save()
            if food.food_group == 'Unknown':
                subject = f"Image does not contains Food"
                message = f"Hello , \nthis is to inform you that your child {food.kid.name}'s food image does not conatain any food  \nThank You"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [kid.parents_email,]
                send_mail( subject, message, email_from, recipient_list )
                print('--------------email sent-----------')
            else:
                print('--------fail---------')
            messages.success(request, f"Food updated successfully!")
            return redirect(f"/foods/{kid.id}")
        else: 
            messages.error(request, f"Something went wrong, Please try again!")
            return redirect(f"/foods/{kid.id}")
    else:
        kid = Kid.objects.get(pk=kid_pk)
        food = Food.objects.get(pk=food_pk)
        form = addFoodForm(request.POST or None, instance = food)
        ctx = {'form': form, 'kid': kid, 'food': food}
        return render(request, 'edit_food.html', ctx)

def delete_Food(request, food_pk, kid_pk):
    food = Food.objects.get(pk=food_pk, kid__pk=kid_pk)
    food.delete()
    messages.success(request, f"Food deleted seccessfully!" )
    return redirect(f"/foods/{kid_pk}")