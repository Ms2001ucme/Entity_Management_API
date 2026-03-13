from django.db import models

# Create your models here.
class VendorProductMapping(models.Model):

    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['vendor', 'product']