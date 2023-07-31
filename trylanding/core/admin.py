from django.contrib import admin
from .models import Slider, Navbar
class NavbarAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']

admin.site.register(Slider)
admin.site.register(Navbar, NavbarAdmin)

