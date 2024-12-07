from django.contrib import admin
from . models import *
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'guruh', 'kurs', 'kitob_soni')
    list_display_links = ('ism','guruh')
    list_editable = ('kurs','kitob_soni')
    list_filter = ('kurs',)
    search_fields = ('ism', 'guruh')

class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = 'olingan_sana'

class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1


# class MuallifAdmin(admin.ModelAdmin):
#     list_display = ('ism','jins', 'tugilgan_sana', 'kitob_soni','tirik')
#     inlines = (KitobInline,)


class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ('ism','ish_vaqti',)
    list_filter = ('ish_vaqti',)


class MuallifAdmin(admin.ModelAdmin):
    list_display = ('ism','tugilgan_sana','jins','kitob_soni','tirik')
    list_display_links = ( 'ism',)
    list_editable = ('kitob_soni','tirik')
    # list_filter = ('tirik')
    search_fields = ('ism',)







admin.site.register(Talaba,TalabaAdmin)
admin.site.register(Muallif,MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record, RecordAdmin)
