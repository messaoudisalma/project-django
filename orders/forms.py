from django import forms

class OrderForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    address1 = forms.CharField(max_length=250)
    address2 = forms.CharField(max_length=250)
    # Ajoutez d'autres champs selon vos besoins
