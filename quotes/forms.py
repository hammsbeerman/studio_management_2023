from django import forms
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import KruegerJobDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class KruegerJobDetailForm(forms.ModelForm):
    class Meta:
        model = KruegerJobDetail
        fields = [
            'jobnumber', 'jobquote', 'company', 'customer', 'description', 'set_per_book', 'pages_per_book', 'qty_of_sheets', 'original_size', 'press_size', 'press_size_per_parent',
            'flat_size', 'finished_size', 'gangup', 'overage', 'output_per_sheet', 'parent_sheets_required', 'side_1_clicks', 'side_2_clicks', 'paper_stock', 'price_per_m'
        ]
        widgets = {
            'set_per_book': forms.NumberInput(attrs={}),
            'pages_per_book': forms.NumberInput(attrs={}),
            'output_per_sheet': forms.TextInput(attrs={'readonly':'readonly'}),
            'qty_of_sheets': forms.TextInput(attrs={'readonly':'readonly'}),
            'parent_sheets_required': forms.TextInput(attrs={'readonly':'readonly'}),
        }

    def clean_jobnumber(self):
        jobnumber = self.cleaned_data.get('jobnumber')
        if not jobnumber:
            raise forms.ValidationError('This field is required')
        return jobnumber


    def clean_company(self):
        company = self.cleaned_data.get('company')
        if not company:
            raise forms.ValidationError('This field is required')
        return company
    
    """def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError('This field is required')
        return description"""
    
    def clean_qty(self):
        qty = self.cleaned_data.get('qty')
        if not qty:
            raise forms.ValidationError('This field is required')
        return qty