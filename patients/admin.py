from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ('first_name', 'last_name', 'date_of_birth', 'contact_number', 'email')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Patient, PatientAdmin)

