from django.contrib import admin
from .models import Tasks

class display(admin.ModelAdmin):
    list_display = ('tasks','is_completed','modified_at')
    search_fields = ('tasks',)
# Register your models here.
admin.site.register(Tasks,display)