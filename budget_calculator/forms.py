from django import forms
from .models import BudgetCalculator
from accounts.models import Destination  # Assuming Destination model is in the accounts app


class BudgetCalculatorForm(forms.ModelForm):
    class Meta:
        model = BudgetCalculator
        fields = [
            'destination',
            'accommodation_cost',
            'transportation_cost',
            'food_cost',
            'activity_cost',
            'number_of_adults',
            'number_of_infants',
        ]
        widgets = {
            'destination': forms.Select(attrs={'class': 'form-control'}),
            'accommodation_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '$0.00','min': 0}
            ),
            'transportation_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '$0.00','min': 0}
            ),
            'food_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '$0.00','min': 0}
            ),
            'activity_cost': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '$0.00','min': 0}
            ),
            'number_of_adults': forms.NumberInput(
                attrs={'class': 'form-control','min': 1}
            ),
            'number_of_infants': forms.NumberInput(
                attrs={'class': 'form-control','min': 0}
            ),
        }
