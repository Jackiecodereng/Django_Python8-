from django import forms

from capital.models import Stock, Purchase, Returned


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product','product_id','price','quantity','date']
        widgets = {

            'date': forms.DateInput(
                attrs={'class': 'datepicker', 'type': 'date', 'min': '2023-01-01', 'max': '2024-12-31'}),
            'quantity': forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '200'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['quantity_bought','sold_by','bought_by']
        widgets = {
            'quantity_bought': forms.NumberInput(attrs={'type':'number','min':'0','max':'100'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ReturnedForm(forms.ModelForm):
    class Meta:
        model = Returned
        fields = ['returned_date','returned_by']





