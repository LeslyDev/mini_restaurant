from django.contrib import admin

from infrastructure.models import *


@admin.register(MenuElement)
class MenuElementAdmin(admin.ModelAdmin):
    pass


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass
