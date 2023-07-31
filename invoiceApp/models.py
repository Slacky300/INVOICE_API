from django.db import models
import uuid

class Invoice(models.Model):

    date= models.DateTimeField(auto_now_add=True)
    invoice_no= models.CharField(max_length=16,unique=True, editable=False)
    customer_name= models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        
        if not self.invoice_no:
            generated_uuid = str(uuid.uuid4())
            self.invoice_no = generated_uuid.replace('-', '')[:16] 
        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):

        return f'{self.customer_name} - {self.invoice_no}'
    

class InvoiceDetail(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,related_name='invoice_detail')
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    price = models.FloatField(default=0)

    def __str__(self):

        return f'{self.invoice} - {self.price}'
    

    
    def save(self, *args, **kwargs):
        # Calculate and set the price before saving
        self.price = self.unit_price * self.quantity
        super(InvoiceDetail, self).save(*args, **kwargs)