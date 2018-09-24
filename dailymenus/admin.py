from django.contrib import admin
from django import forms
from .models import DailyMenu, MenuAlternative


class DailyMenuForm(forms.ModelForm):

    class Meta:
        model = DailyMenu
        exclude = []

class MenuAlternativeInline(admin.TabularInline):
    
    model = MenuAlternative
    min_num = 1
    extra = 0

class DailyMenuAdmin(admin.ModelAdmin):

    form = DailyMenuForm
    inlines = [MenuAlternativeInline,]
    exclude = []

admin.site.register(DailyMenu, DailyMenuAdmin)