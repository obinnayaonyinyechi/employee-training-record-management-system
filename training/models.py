from django.db import models


class TrainingRecord(models.Model):

    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    training_title = models.CharField(max_length=200)

    employee_name = models.CharField(max_length=150)

    training_date = models.DateField()

    training_duration = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Training duration in hours"
    )

    training_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Planned'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-training_date']

    def __str__(self):
        return f"{self.employee_name} - {self.training_title}"