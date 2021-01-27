from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from infrastructure.models import *
from infrastructure.forms import *


def start_redirect(request):
    return redirect('index', permanent=True)


def index(request):
    return render(request, 'index.html')


def food_list(request):
    food = MenuElement.objects.filter(element_type='food').all()
    return render(request, 'food_list.html', context={'food': food})


def drink_list(request):
    drinks = MenuElement.objects.filter(element_type='drink').all()
    return render(request, 'drink_list.html', context={'drinks': drinks})


def tables_info(request):
    free_table_info = Table.objects.filter(status='free').all().order_by('size')
    return render(request, 'tables_info.html', context={'free_table_info': free_table_info})


def busy_tables_info(request):
    busy_table_info = Table.objects.filter(status='busy').all()
    return render(request, 'busy_tables_info.html', context={'busy_table_info': busy_table_info})


def book_table(request, table_id):
    form = TableForm()
    if request.method == 'GET':
        return render(request, 'book_table.html', context={'form': form, 'id': table_id})
    else:
        Table.objects.filter(id=table_id).update(time=request.POST['time'],
                                                 status='busy',
                                                 owner_name=request.POST['owner_name'],
                                                 owner_number=request.POST['owner_number'])
        return HttpResponseRedirect(reverse_lazy('busy_tables_info_url'))
