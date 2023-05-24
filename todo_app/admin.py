from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_completed", "updated_at")
    search_fields = ("title",)
