
from django.urls import path
from . import views
urlpatterns = [

    path('invoice/',views.InvoiceViewSet.as_view(), name="invoice")

]    


