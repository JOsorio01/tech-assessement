from django.contrib import admin

from core import models


class NamesMatchAdmin(admin.ModelAdmin):
    list_display = ("db_name", "match_name")


class FileTemplateAdmin(admin.ModelAdmin):
    list_display = ("template_name", "active", "match")

    def match(self, obj):
        return ", ".join([a.db_name for a in obj.match_names.all()])


admin.site.register(models.NamesMatch, NamesMatchAdmin)
admin.site.register(models.FileTemplate, FileTemplateAdmin)
