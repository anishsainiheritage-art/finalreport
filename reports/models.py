# reports/models.py

from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Report(models.Model):
    buyer = models.CharField(max_length=100, blank=True, null=True)
    po_no = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default="draft")
    
    email = models.EmailField(blank=True, null=True)
    inspection_date = models.DateField(blank=True, null=True)
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    item_code = models.CharField(max_length=100, blank=True, null=True)
    internal_pi_no = models.CharField(max_length=100, blank=True, null=True)
    collection = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    materials = models.CharField(max_length=100, blank=True, null=True)
    item_size = models.CharField(max_length=100, blank=True, null=True)
    carton_size = models.CharField(max_length=100, blank=True, null=True)
    net_weight = models.CharField(max_length=100, blank=True, null=True)
    gross_weight = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    images_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)