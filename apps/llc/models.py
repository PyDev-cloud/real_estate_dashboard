from django.db import models
from apps.investors.models import InvestorProfile

class LLC(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class LLCInvestor(models.Model):
    llc = models.ForeignKey(LLC, on_delete=models.CASCADE)
    investor = models.ForeignKey(InvestorProfile, on_delete=models.CASCADE)
    ownership_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.DateField()

    class Meta:
        unique_together = ('llc', 'investor')

    def __str__(self):
        return f"{self.investor} - {self.llc}"