from django.contrib import admin
from .models import NseSettings, NseReport
# Register your models here.

admin.site.register(NseSettings)
admin.site.register(NseReport)