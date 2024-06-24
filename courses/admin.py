from django.contrib import admin
from .models import Course , User , Module , Subject
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug']
    prepopulated_fields = {'slug':('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display    = ['title' , 'subject' , 'created']
    list_filter     = [ 'subject' , 'created']
    search_fields   = ['title' , 'subject' , 'created']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ModuleInline]