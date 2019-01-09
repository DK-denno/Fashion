from django.contrib import admin

# Register your models here.
from .models import Posts,Category

class AdminCat(admin.ModelAdmin):
    filter_horizontal=('category',)

admin.site.register(Posts,AdminCat)
admin.site.register(Category)
# admin.site.register(Location)
