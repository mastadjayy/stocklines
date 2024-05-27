from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import (
#    WarehouseType,
    Warehouse
)


class WarehouseForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Warehouse
        fields = ["warehouse_name", "warehouse_type", "surface_area",
                  "fill_rate", "volume", "capacity", "comment", "is_active"]
        widgets = {
            "warehouse_name": forms.TextInput(attrs={'class': 'textinput form-control'}),
            "is_active": forms.CheckboxInput
        }
        error_messages = {
            'warehouse_name': {'required': ('Ce champ est obligatoire.'), 'unique': ('Ce magasin existe déjà.')},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_show_labels = False
        self.fields['warehouse_name'].label = "Nom Magasin"
        self.fields['warehouse_type'].label = "Type Magasin"
        self.fields['surface_area'].label = "Superficie (m2)"
        self.fields['fill_rate'].label = "Taux Remplissage Magasin"
        self.fields['volume'].label = "Capacité Volume Magasin"
        self.fields['capacity'].label = "Capacité Tonnage Magasin"
        self.fields['comment'].label = "Commentaire"
        self.fields['is_active'].label = "Actif"
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Valider', css_class='btn btn-success'))
