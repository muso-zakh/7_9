from django.contrib import admin

# Register your models here.

from .models import Category, Term


admin.site.register(Category)
admin.site.register(Term)