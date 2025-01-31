from django import forms
from accounts.models import Destination


# Destination Form
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = [
            'name', 'country', 'description', 'best_time_to_visit',
            'budget_type', 'image', 'is_favorite'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'best_time_to_visit': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'budget_type': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
            'is_favorite': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }


# Destination Search
class DestinationSearchForm(forms.Form):
    query = forms.CharField(required=False, label="Search Destinations")
