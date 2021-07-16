from django.contrib import admin
from .models import Contacttuber
# Register your models here.
class ContacttuberAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','subject')
    list_display_links=('id','name','phone')

admin.site.register(Contacttuber,ContacttuberAdmin)