from django.contrib import admin
from .models import realdata,syntheticdata,modelData,project,parameters
# Register your models here.
@admin.register(realdata)
class realdataModel(admin.ModelAdmin):
    list_display=['real_data']
@admin.register(project)
class projectModel(admin.ModelAdmin):
    list_display=['proj']
@admin.register(modelData)
class projectModel(admin.ModelAdmin):
    list_display=['name']
@admin.register(parameters)
class prametersModel(admin.ModelAdmin):
    list_display=['name','batch_size','training_cycles']
@admin.register(syntheticdata)
class SyntheticdataModel(admin.ModelAdmin):
    list_display=['name','synthetic_data']
