from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import Backscratcher


admin.site.register(Backscratcher)
TokenAdmin.raw_id_fields = ('user',)
