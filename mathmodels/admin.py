from django.contrib import admin
from .models import MathModels

class MathModelsAdmin(admin.ModelAdmin):
    class Meta:
        model = MathModels
        
admin.site.register(MathModels, MathModelsAdmin)
    
