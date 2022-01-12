from django.contrib import admin
from accounts.models import User, Contest


class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)
admin.site.register(Contest)

