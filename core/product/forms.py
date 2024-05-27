from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Product


class ProductForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Product
        fields = ['product_name']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'textinput form-control'})
        }
        error_messages = {
            'product_name': {'required': ('Ce champ est obligatoire !'), 'unique': ('Ce produit existe déjà !')},
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['product_name'].label = "Nom"
        self.helper.add_input(Submit('submit', 'Valider', css_class='btn btn-success'))
