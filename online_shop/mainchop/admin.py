from django.contrib import admin
from django.forms import ModelChoiceField
from .models import *




class BoilerAdmin(admin.ModelAdmin):


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='boiler'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PompAdmin(admin.ModelAdmin):


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='pomp'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Boiler, BoilerAdmin)
admin.site.register(Pomp, PompAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
