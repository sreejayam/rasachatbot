
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, LandRegistrationInfo, LandInfo


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone_number', 'password', 'gender')}),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'age',
                'aadhar_number',
                'krishibhavan',
                'panchayath',
                'district',
                'email',  # If you still want to keep email field visible in the admin
                'pincode',
            ),
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'password1',
                'password2',



                'gender',
                'phone_number',
                'aadhar_number',

                'age',
                'krishibhavan',
                'panchayath',
                'district',
                'email',  # If you still want to keep email field visible in the admin
                'pincode',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    list_display = ('phone_number', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'gender')
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('phone_number',)
    filter_horizontal = ()


# Register the CustomUser model with the CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin)

class LandInfoAdmin(admin.StackedInline):
    model = LandInfo


class LandRegistrationInfoAdmin(admin.ModelAdmin):
    inlines = [LandInfoAdmin]
    list_display = ['phone_number', ]

    search_fields = ['phone_number__phone_number']  # Enable searching by phone_number


admin.site.register(LandRegistrationInfo, LandRegistrationInfoAdmin)
