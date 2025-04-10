from django.db import models

# Create your models here.

SERVICES = [
    ('Property', 'Property'),
    ('Loan Security', 'Loan Security'),
    ('Rental', 'Rental'),
    ('Deal Advisory', 'Deal Advisory'),
    ('Insurance', 'Insurance'),
    ('Investment', 'Investment'),
    ('Legal & Tax', 'Legal & Tax'),
]


class Quote(models.Model):
    Service = models.CharField(max_length=64, null=True, choices=SERVICES)
    Name = models.CharField(max_length=64, primary_key=True)
    Email = models.EmailField(null=True)
    Site_Address = models.CharField(max_length=64)

    #utility Fields
    created_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
