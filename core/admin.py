from django.contrib import admin
from .models import Term, SearchLog, SuggestLog, FeedbackLog, ImproveLog


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('term', 'acronym', 'definition')
    ordering = ['term']


@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'search_phrase')
    readonly_fields = ('timestamp', 'search_phrase')
    ordering = ['-timestamp']


@admin.register(ImproveLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'term', 'comments')
    readonly_fields = ('timestamp', 'term', 'comments')
    ordering = ['-timestamp']


@admin.register(SuggestLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'name', 'dept', 'suggestion')
    readonly_fields = ('timestamp', 'name', 'dept', 'suggestion')
    ordering = ['-timestamp']


@admin.register(FeedbackLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'name', 'dept', 'feedback')
    readonly_fields = ('timestamp', 'name', 'dept', 'feedback')
    ordering = ['-timestamp']


admin.site.site_header = "Techxicon Administration"
admin.site.site_title = "Techxicon Site Admin"