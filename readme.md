# Invoice Django Application

The Invoice Django Application is a Django Rest Framework (DRF) application that provides APIs for managing invoices and their details. It consists of two models, `Invoice` and `InvoiceDetail`, representing invoice information and invoice line items, respectively. The application utilizes Model Viewsets and Model Serializers to simplify the API creation process and also implements a nested serializer to handle invoice details in the payload.

## Table of Contents

- [Setup](#setup)
- [Models](#models)
- [Serializers](#serializers)
- [API Endpoints](#api-endpoints)

## Setup

To run the Invoice Django Application on your local machine, follow these steps:

1. Clone the repository:

``` bash
git clone https://github.com/your-username/invoice-app.git
cd invoice-app

    Create and activate a virtual environment (optional, but recommended):
```
```bash

python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
```
Install the required dependencies:

```bash

pip install -r requirements.txt
```
Run database migrations:

```bash

python manage.py makemigrations
python manage.py migrate
```
Start the development server:

```bash

python manage.py runserver
```
The Invoice application should now be running on http://localhost:8000/.

## Models

The Invoice application consists of two Django models:
Invoice Model

Fields:
    date: The date of the invoice (added at the time of creation).
    invoice_no: The unique identifier for the invoice(automatically created using uuid at the time of creation).
    customer_name: The name of the customer associated with the invoice.

InvoiceDetail Model

    Fields:
        invoice: A foreign key to the Invoice model, representing the associated invoice.
        description: A description of the item in the invoice detail.
        quantity: The quantity of the item in the invoice detail.
        unit_price: The unit price of the item in the invoice detail.
        price: The calculated price for the item (unit_price * quantity). Note: This field is automatically calculated using the model's save method.

## Serializers

The application uses Django Rest Framework (DRF) serializers to handle data serialization and deserialization. Two serializers are defined:
InvoiceSerializer

    Serializes and deserializes Invoice objects.
    Includes a nested serializer, InvoiceDetailSerializer, to handle invoice details.

InvoiceDetailSerializer

    Serializes and deserializes InvoiceDetail objects.

## API Endpoints

The Invoice application provides the following API endpoints:

    GET /invoices/: Retrieves a list of all invoices.
    POST /invoices/: Creates a new invoice along with associated invoice details in the payload.

    eg. payload data:
    { 
      "customer_name": "John Smith",
      "invoice_detail": [
          {
            "description": "Product A",
            "unit_price": 50,
            "quantity": 5
          },
          {
            "description": "Product B",
            "unit_price": 30,
            "quantity": 10
          }
        ]
    }

## Test Cases

The application includes test cases that cover various scenarios, including creating invoices, retrieving invoices, and handling invalid invoice data. To run the tests, use the following command:

bash

python manage.py test
