from django.contrib import admin
from pages.models import Home
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    pass

admin.site.register(Home, HomeAdmin)