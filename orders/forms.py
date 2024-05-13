from django import forms

class CartAddForm(forms.Form):
    quantily = forms.IntegerField(min_value=1, max_value=10)
