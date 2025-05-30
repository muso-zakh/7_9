from django.contrib import admin

# Register your models here.

from .models import Omonim, Details


admin.site.register(Omonim)
admin.site.register(Details)