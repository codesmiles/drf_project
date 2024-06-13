from .views import InitiatePaymentView
from django.urls import path

app_name = "plans"

urlpatterns = [  
    path('initiate-payment/', InitiatePaymentView.as_view(), name='initiate-payment'),
    # path('flutterwave-webhook/', FlutterwaveWebhookView.as_view(), name='flutterwave-webhook'),
]