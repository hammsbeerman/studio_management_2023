from django.db import models
from customers.models import Customer

class KruegerJobDetail(models.Model):
    class JobQuote(models.TextChoices):
        JOB = "Job"
        QUOTE = "Quote"

    class Company(models.TextChoices):
        LK = "LK"
        KRUEGER = "KRUEGER"

    jobnumber = models.CharField('Job Number', max_length=100, blank=False, null=False)
    jobquote = models.CharField('Workorder or Quote', max_length=100, choices=JobQuote.choices, blank=False, null=False)
    company = models.CharField('Company', max_length=100, choices=Company.choices, blank=False, null=False)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField('Job Description', max_length=100, blank=True, null=True)
    set_per_book = models.PositiveIntegerField('Sets per Book', blank=True, null=True)
    pages_per_book = models.PositiveBigIntegerField('Pages per Book', blank=True, null=True)
    qty_of_sheets = models.CharField('Qty of Sheets', max_length=10, blank=True, null=True)
    original_size = models.CharField('Original Size', max_length=100, blank=True, null=True)
    press_size = models.CharField('Press Size', max_length=100, blank=True, null=True)
    press_size_per_parent = models.CharField('Press sheets / Parent', max_length=100, blank=True, null=True)
    flat_size = models.CharField('Flat Size', max_length=100, blank=True, null=True)
    finished_size = models.CharField('Finished Size', max_length=100, blank=True, null=True)
    gangup = models.PositiveBigIntegerField('Gangup', blank=True, null=True)
    overage = models.PositiveBigIntegerField('Overage', blank=True, null=True)
    output_per_sheet = models.CharField('Output per Parent Sheet', max_length=10, blank=True, null=True)
    parent_sheets_required = models.CharField('Parent Sheets Required', max_length=10, blank=True, null=True)
    side_1_clicks = models.CharField('Side 1 Clicks', max_length=100, blank=True, null=True)
    side_2_clicks = models.CharField('Side 2 Clicks', max_length=100, blank=True, null=True)
    paper_stock = models.CharField('Paper Stock', max_length=100, blank=True, null=True)
    price_per_m = models.CharField('Price per M', max_length=100, blank=True, null=True)
    dateentered = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.jobnumber + ' ' + self.company + ' ' + self.description
