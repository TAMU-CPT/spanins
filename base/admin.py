from django.contrib import admin
from .models import Host, Spanin, Phage

class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SpaninAdmin(admin.ModelAdmin):
    list_display = ('id', 'sequence', 'accession')

class PhageAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'name', 'accession', 'spanin_type', 'i_spanin', 'o_spanin', 'u_spanin')

admin.site.register(Host, HostAdmin)
admin.site.register(Spanin, SpaninAdmin)
admin.site.register(Phage, PhageAdmin)
