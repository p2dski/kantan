from django.contrib import admin
from .models import Regression

class RegressionAdmin(admin.ModelAdmin):
    class Meta:
        model = Regression
        
admin.site.register(Regression, RegressionAdmin)
    
