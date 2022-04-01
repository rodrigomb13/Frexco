from django.contrib import admin

from .models import Region, Fruit


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('region','nameFruit')
