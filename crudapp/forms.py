from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["oid", "fname", "lname", "price", "mail", "addr"]
        widgets = {
            "oid": forms.NumberInput(attrs={"placeholder": "101"}),
            "fname": forms.TextInput(attrs={"placeholder": "Prosenjeet"}),
            "lname": forms.TextInput(attrs={"placeholder": "Shil"}),
            "price": forms.NumberInput(attrs={"placeholder": "10000"}),
            "mail": forms.EmailInput(attrs={"placeholder": "abc@xyz.com"}),
            "addr": forms.Textarea(attrs={"placeholder": "Ukraine", "rows": 3}),
        }
