from django.db import models
from apps.investors.models import InvestorProfile
from apps.projects.models import Project

class Reinvestment(models.Model):
    investor = models.ForeignKey(InvestorProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    original_amount = models.DecimalField(max_digits=12, decimal_places=2)
    reinvested_amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_out_amount = models.DecimalField(max_digits=12, decimal_places=2)

    date = models.DateField()

    def __str__(self):
        return f"{self.investor} reinvested"