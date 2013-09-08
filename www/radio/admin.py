from django.contrib import admin

from models import *

class StationAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Category)
admin.site.register(Network)
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Source)
admin.site.register(Station, StationAdmin)

