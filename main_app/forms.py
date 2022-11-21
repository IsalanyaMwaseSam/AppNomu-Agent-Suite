from django import forms
from intl_tel_input.widgets import IntlTelInputWidget

class AirtimeForm(forms.Form):
    amount = forms.IntegerField(label='Enter Amount')
    tel_number = forms.CharField(widget=IntlTelInputWidget(attrs={'id': 'phone'}))


class DataForm(forms.Form):
    amount = forms.IntegerField(label='Enter Amount')
    tel_number = forms.CharField(widget=IntlTelInputWidget(attrs={'id': 'phone'}))