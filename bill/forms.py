from django.forms import ModelForm
from django import forms
from bill.models import order,product,purchase

class ordercreateform(ModelForm):
    class Meta:
        model=order
        fields=['bill_number','customer_name','phone_number']
        widgets = {
            'bill_number': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class orderlinesform(forms.Form):
    bill_number=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_quantity=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_name=purchase.objects.all().values_list('product__product_name')
    result=[(tp[0],tp[0]) for tp in product_name]
    product_name=forms.ChoiceField(choices=result)


class productcreateform(ModelForm):
    class Meta:
        model=product
        fields='__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class purchasecreateform(ModelForm):
    class Meta:
        model=purchase
        fields='__all__'
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_price': forms.TextInput(attrs={'class': 'form-control'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.TextInput(attrs={'class': 'form-control'}),
        }