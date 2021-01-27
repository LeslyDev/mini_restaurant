from django.urls import path

from infrastructure.views import *

urlpatterns = [
    path('home_page/', index, name='index'),
    path('food/', food_list, name='food_list_url'),
    path('drinks/', drink_list, name='drink_list_url'),
    path('book_table/', book_table, name='book_table_url')
]
