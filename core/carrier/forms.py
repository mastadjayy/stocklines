from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Carrier


class CarrierForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Carrier
        fields = ['carrier_name']
        widgets = {
            'carrier_name': forms.TextInput(attrs={'class': 'textinput form-control'}),
        }
        error_messages = {
            'carrier_name': {'required': ('Ce champ est obligatoire !'), 'unique': ('Ce transporteur existe déjà !')},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['carrier_name'].label = "Nom du Transporteur"
        self.helper.add_input(Submit('submit', 'Valider', css_class='btn btn-success'))
