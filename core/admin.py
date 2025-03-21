from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # fields=['name','price','description',"discount","owner","quantity"] # This will change the order of fields in the admin page
    exclude=["created_at"]
    fieldsets=[
        ("Product Information",{"fields":["name","price","description","discount","quantity"]}),
        ("Owner Information",{"fields":["owner"],"classes":["collapse"]})
    ]
    list_display=('name','price','description','owner','quantity','created_at')
    list_filter=['price','quantity','created_at']
    search_fields=['name','description']
    
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(CustomUser)
admin.site.register(Product,ProductAdmin)