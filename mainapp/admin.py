from django.contrib import admin
from mainapp.models import Token, UserTokens

admin.site.register(Token)
admin.site.register(UserTokens)