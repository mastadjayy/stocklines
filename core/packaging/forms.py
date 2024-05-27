from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Packaging


class PackagingForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Packaging
        fields = ['pack_type']
        widgets = {
            'pack_type': forms.TextInput(attrs={'class': 'textinput form-control'}),
        }
        error_messages = {
            'pack_type': {'required': ('Ce champ est obligatoire !'), 'unique': ('Cet emballage existe déjà !')},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['pack_type'].label = "Emballager"
        self.helper.add_input(Submit('submit', 'Valider', css_class='btn btn-success'))
