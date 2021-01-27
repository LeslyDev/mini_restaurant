from django.urls import path

from infrastructure.views import *

urlpatterns = [
    path('home_page/', index, name='index'),
    path('food/', food_list, name='food_list_url'),
    path('drinks/', drink_list, name='drink_list_url'),
    path('tables_info/', tables_info, name='tables_info_url'),
    path('book_table/<int:table_id>/', book_table, name='book_table_url'),
    path('busy_tables_info/', busy_tables_info, name='busy_tables_info_url')
]
