from django.db import models
from apps.llc.models import LLC
from apps.investors.models import InvestorProfile

class Project(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('construction', 'Construction'),
        ('listed', 'Listed'),
        ('sold', 'Sold'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    property_address = models.TextField()
    llc = models.ForeignKey(LLC, on_delete=models.SET_NULL, null=True, blank=True)

    total_budget = models.DecimalField(max_digits=15, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    start_date = models.DateField()
    estimated_end_date = models.DateField()
    actual_end_date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def remaining_budget(self):
        return self.total_budget - self.amount_spent

    def __str__(self):
        return self.name
    


class InvestorProject(models.Model):
    investor = models.ForeignKey(InvestorProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    ownership_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ('investor', 'project')

    def __str__(self):
        return f"{self.investor} -> {self.project}"