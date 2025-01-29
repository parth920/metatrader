
from django import forms

class MasterLoginForm(forms.Form):
    master_login = forms.CharField(label='Master Login')
    master_password = forms.CharField(widget=forms.PasswordInput(), label='Master Password')

class TradingParametersForm(forms.Form):
    sl_point = forms.FloatField(label='Stop Loss Point')
    tp_point = forms.FloatField(label='Take Profit Point')
    lot_size = forms.FloatField(label='Lot Size')
    price_interval = forms.FloatField(label='Price Interval')
    script_choice = forms.ChoiceField(choices=[
        ('Buy-Sell', 'Buy-Sell'),
        ('Only Buy', 'Only Buy'),
        ('Only Sell', 'Only Sell'),
    ],label='Script Choice')

# class PinForm(forms.Form):
#     pin = forms.CharField(max_length=6, widget=forms.PasswordInput(attrs={'placeholder': 'Enter PIN'}))
