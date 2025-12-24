from django.contrib import admin
from .models import Account

# admin.site.register(Account)

@admin.register(Account)
class AdminRestPassword(admin.ModelAdmin):
    list_display = [
        "old_password",
        "new_password",
    ]
    