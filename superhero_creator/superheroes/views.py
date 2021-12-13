from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from .models import Superhero

# Create your views here.
def index(request):
    # query set
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    # instance of the superhero class
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)
    
def create(request):
    if request.method == "POST":
        # save the form contents as a new db object
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary_ability')
        secondary = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def delete(request):
    if request.method == "POST":
        # save the form contents as a new db object
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary_ability')
        secondary = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        delete_hero.delete()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/delete.html')

def edit(request):
    if request.method == "POST":
        # save the form contents as a new db object
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary_ability')
        secondary = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        edit_hero.edit()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/edit.html')
    