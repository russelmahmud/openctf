from django.contrib import admin

from .models import Gender, PlayerType
# Register your models here.
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(PlayerType)
class PlayerTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    list_display = ('name', )
