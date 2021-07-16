from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40"/>', format(object.photo.url))
    list_display=('id','first_name','myphoto',  'role', 'created_date')
    list_display_links=('id','first_name',)
    search_fields=('first_name','role')
    list_filter=('role',)


class SliderAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="250"/>', format(object.photo.url))
    list_display=('headline', 'myphoto', 'button_text',)
    list_display_links=('headline', 'button_text',)


admin.site.register(Slider,SliderAdmin)
admin.site.register(Team, TeamAdmin)

