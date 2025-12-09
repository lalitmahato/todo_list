from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add the new fields to the admin interface
    fieldsets = UserAdmin.fieldsets + (
        ('Personal Info', {'fields': ('date_of_birth', 'gender', 'photo', 'bio', 'phone_number', 'address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)