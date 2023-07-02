from django.urls import path

from . import views

app_name = "currency"

urlpatterns = [path("", views.CurrencyFormView.as_view(), name="currency_form")]
