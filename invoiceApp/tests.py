from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import InvoiceDetail
from .serializers import InvoiceSerializer


class InvoiceAPITestCase(TestCase):
    

    def test_invalid_invoice_data(self):
        invalid_invoice_data = {
            "date": "2023-07-16",
            "invoice_no": "",  # Empty invoice number
            "customer_name": "John Doe",
            "invoice_details": [
                {
                    "description": "Product A",
                    "quantity": 2,
                    "unit_price": "10.00"
                }
            ]
        }
        response = self.client.post(reverse('invoice'), invalid_invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)





