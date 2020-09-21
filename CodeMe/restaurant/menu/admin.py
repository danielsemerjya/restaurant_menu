from django.contrib import admin


# Register your models here.
from menu.models import Dish, Category

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "pub_date", "price"] #Pola wyswietlane na liscie
    list_editable = ["price"]

admin.site.register(Category)