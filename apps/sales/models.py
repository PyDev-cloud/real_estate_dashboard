from django.db import models
from apps.projects.models import Project

class Sale(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    selling_costs = models.DecimalField(max_digits=15, decimal_places=2)
    closing_date = models.DateField()

    def net_profit(self):
        return self.sale_price - self.selling_costs - self.project.amount_spent

    def __str__(self):
        return f"Sale - {self.project}"