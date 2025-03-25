from django.contrib import admin

# Register your models here.

from .models import Blog
from .models import category


admin.site.register(Blog)
admin.site.register(category)