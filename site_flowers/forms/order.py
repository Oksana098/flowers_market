from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone
import datetime
from site_flowers.models import Order


class OrderForm(forms.ModelForm):
    date_order = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Order
        fields = ('date_order', 'name', 'phone', 'email', 'count', 'delivery', 'delivery_address', 'flowers')
        exclude = ['date_created']

    def clean_date_order(self):
        get_data = self.cleaned_data['date_order']
        if get_data < datetime.date.today():
            raise forms.ValidationError('Vvedy suka virny daty!!! Vysylaj bratkiv')

        return get_data