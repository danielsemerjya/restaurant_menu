from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Dish, Category

# Create your views here.

def hello(request, name):

    return HttpResponse(f"Hello {name}!")

def add(request, num_1, num_2):

    result = int(num_1) + int(num_2)

    return HttpResponse(f"Answer: {result}!")


def about(request):

    return render(request, "about.html", {})

def dishes_all(request):
    categories = Category.objects.all()
    my_dishes = Dish.objects.all()

    ctx = {
        "categories" :categories,
        "dishes": my_dishes,
    }
    return render(request, "menu.html", ctx)


def dishes_by_category(request, category_id):
    categories = Category.objects.all()

    category = Category.objects.get(id=category_id)
    my_dishes = Dish.objects.filter(category=category)
        

    ctx = {
        "categories" :categories,
        "dishes": my_dishes,
    }

    return render(request, "menu.html", ctx)