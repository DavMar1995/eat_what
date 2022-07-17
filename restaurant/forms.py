from django import forms
from .models import Restaurant


class RestaurantCreationForm(forms.ModelForm):
    
    class Meta:
        model = Restaurant
        fields = ['name']
        # widget = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'})
        # }

class RestaurantUpdateForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'