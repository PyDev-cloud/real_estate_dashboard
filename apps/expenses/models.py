from django.db import models
from apps.projects.models import Project

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('purchase', 'Purchase'),
        ('construction', 'Construction'),
        ('materials', 'Materials'),
        ('labor', 'Labor'),
        ('utilities', 'Utilities'),
        ('insurance', 'Insurance'),
        ('other', 'Other'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    vendor_name = models.CharField(max_length=255, blank=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_paid = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.project} - {self.amount}"