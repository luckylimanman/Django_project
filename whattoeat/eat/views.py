from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import random

from .models import Restaurant


def index(request):
    return render(request, 'eat/index.html')


def eat_result(request):
    eatresult = random.choice(Restaurant.objects.all())
    return render(request, 'eat/eat_result.html', {'eatresult': eatresult})


def add_restaurant(request):
    # return render(request, 'eat/view_restaurant.html')
    return render(request, 'eat/add_restaurant.html')


def view_restaurant(request):
    restuarant_all = Restaurant.objects.all()
    return render(request, 'eat/view_restaurant.html', {'restuarant_all': restuarant_all})
