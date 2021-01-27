from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from infrastructure.models import *
from infrastructure.forms import *


def start_redirect(request):
    return redirect('index', permanent=True)


def index(request):
    return render(request, 'index.html')


def food_list(request):
    food = MenuElement.objects.filter(element_type='food').all()
    return render(request, 'food_list.html', context={'food': food})


def food_detail(request, food_id):
    food = MenuElement.objects.get(id=food_id)
    return render(request, 'food_detail.html', context={'food': food})


def drink_list(request):
    drinks = MenuElement.objects.filter(element_type='drink').all()
    return render(request, 'drink_list.html', context={'drinks': drinks})


def drink_detail(request, drink_id):
    return render(request, 'drink_detail.html')


def book_table(request):
    form = TableForm()
    template = loader.get_template('book_table.html')
    data = {'form': form}
    if request.method == 'GET':
        return HttpResponse(template.render(data, request))
    else:
        Table.objects.update(size=request.POST['size'],
                             # time=request.POST['time'],
                             status='busy',
                             owner_name=request.POST['owner_name'],
                             owner_number=request.POST['owner_number'])
        return redirect('/list/')
