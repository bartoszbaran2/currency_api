from django import forms
from django.utils import timezone


class CurrencyForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    currency = forms.MultipleChoiceField(choices=[], widget=forms.SelectMultiple)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and start_date < timezone.datetime(2005, 1, 2).date():
            self.add_error("start_date", "Start date cannot be earlier than 2005-01-02.")

        if start_date and start_date > timezone.now().date():
            self.add_error("start_date", "Start date cannot be in the future.")

        if end_date and end_date > timezone.now().date():
            self.add_error("end_date", "End date cannot be in the future.")

        if end_date >= timezone.now().date():
            self.add_error("end_date", "End date must be earlier than today.")

        if start_date and end_date and end_date < start_date:
            self.add_error("end_date", "End date cannot be earlier than start date.")

        return cleaned_data
