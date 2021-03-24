from django.contrib import admin
from .models import Product, Level

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'skill',
        'difficulty',
        'description',
        'price',
        'rating',
        'image',
        'resource',
    )

    ordering = ('name',)


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Level, LevelAdmin)