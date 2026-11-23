from django import forms
from .models import TrainingRecord


class TrainingRecordForm(forms.ModelForm):

    class Meta:
        model = TrainingRecord

        fields = [
            'training_title',
            'employee_name',
            'training_date',
            'training_duration',
            'training_status',
        ]

        widgets = {
            'training_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter training title'
            }),

            'employee_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter employee full name'
            }),

            'training_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'training_duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter duration in hours',
                'min': '0.01',
                'step': '0.01'
            }),

            'training_status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def clean_training_duration(self):
        duration = self.cleaned_data['training_duration']

        if duration <= 0:
            raise forms.ValidationError(
                'Training duration must be greater than zero.'
            )

        return duration