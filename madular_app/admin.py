from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import *
from django.apps import apps

models = apps.get_models()


admin.site.register(Products)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(PageShots)

admin.site.site_title = "TOO Modular.kz"
admin.site.site_header = "TOO Modular.kz"