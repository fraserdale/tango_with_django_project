from django.contrib import admin
from django.contrib import admin
from rango.models import Category, Page

# Add in this class to customise the Admin Interface 
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	# Update the registration to include this customised interface

admin.site.register(Category, CategoryAdmin)

# Register your models here.
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

admin.site.register(Page, PageAdmin)

