from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display =  ['title', 'formated_created_date']


    def formated_created_date(self, obj):
        return obj.created.strftime('( %H:%M ) [%Y/%m/%d]')
    formated_created_date.short_description = 'Created'