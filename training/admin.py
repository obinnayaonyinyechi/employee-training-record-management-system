from django.contrib import admin
from .models import TrainingRecord


@admin.register(TrainingRecord)
class TrainingRecordAdmin(admin.ModelAdmin):

    list_display = (
        'training_title',
        'employee_name',
        'training_date',
        'training_duration',
        'training_status',
    )

    list_filter = (
        'training_status',
        'training_date',
    )

    search_fields = (
        'training_title',
        'employee_name',
    )

    ordering = ('-training_date',)