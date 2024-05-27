from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Client


# Client Form
class ClientForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Client
        fields = ['client_name', 'client_ref', 'client_address', 'client_email', 'client_phone', 'products']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'textinput form-control'}),
            'client_address': forms.TextInput(attrs={'class': 'textinput form-control'}),
            'client_email': forms.EmailInput(attrs={'class': 'textinput form-control'}),
            'client_phone': forms.TextInput(attrs={'class': 'textinput form-control'}),
            'products': forms.CheckboxSelectMultiple(attrs={'class': 'textinput form-control'}),
        }
        error_messages = {
            'client_name': {'required': ('Ce champ est obligatoire.'), 'unique': ('Ce produit existe déjà.')},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['client_name'].label = "Nom du Client"
        self.fields['client_ref'].label = "Référence client"
        self.fields['client_address'].label = "Addresse du Client"
        self.fields['client_email'].label = "Email du Client"
        self.fields['client_phone'].label = "Numéro de Téléphone du Client"
        self.helper.add_input(Submit('submit', 'Valider', css_class='btn btn-success'))