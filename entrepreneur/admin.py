from django.contrib import admin

# Register your models here.
from .models import Row, Cow, Duplicate_cow

class RowAdmin(admin.ModelAdmin):
    list_display = ('id','name_of_the_entrepreneur','district','upazilla','village','mobile','last_updated_date')
    list_display_links = ('id','name_of_the_entrepreneur')
    list_per_page = 10
    search_fields = ('name_of_the_entrepreneur', 'id', 'district')
    #list_filter = ('gender', 'date_added')
admin.site.register(Row,RowAdmin)

class CowAdmin(admin.ModelAdmin):
    list_display = ('id','name_of_cow','purchase_date','breed','color','weight','date_of_birth')
    list_display_links = ('id','name_of_cow')
    list_per_page = 10
    search_fields = ('name_of_cow', 'id', 'breed')
admin.site.register(Cow,CowAdmin)
class Duplicate_cowAdmin(admin.ModelAdmin):
    # list_display = ('id','name_of_cow','purchase_date','breed','color','weight','date_of_birth','last_updated_date')
    # list_display_links = ('id','name_of_cow')
    list_per_page = 10
    search_fields = ('name_of_cow', 'id', 'breed')
admin.site.register(Duplicate_cow,Duplicate_cowAdmin)