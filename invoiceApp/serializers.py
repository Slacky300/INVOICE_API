from . models import *
from rest_framework import serializers


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description','quantity','unit_price']

class InvoiceSerializer(serializers.ModelSerializer):

    invoice_detail = InvoiceDetailSerializer(many=True,write_only=True)

    class Meta:
        model = Invoice
        fields = ['id','date', 'invoice_no', 'customer_name', 'invoice_detail']

    def create(self, validated_data):
        invoice_detail = validated_data.pop('invoice_detail')
        invoice = Invoice.objects.create(**validated_data)

        for inv_det in invoice_detail:
            InvoiceDetail.objects.create(invoice=invoice, **inv_det)

        return invoice


