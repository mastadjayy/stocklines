# forms.py
from django import forms
from crispy_forms.helper import FormHelper

from .models import StockIn, StockOut


class BaseStockForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = None  # Set this to StockIn or StockOut in subclasses
        fields = ['product', 'warehouse', 'client', 'quantity', 'flux']


class StockInForm(BaseStockForm):
    class Meta(BaseStockForm.Meta):
        model = StockIn
        fields = ['product', 'warehouse', 'client', 'quantity', 'type_gestion',
                  'campagne', 'date_entry', 'num_contrat', 'comment', 'carrier',
                  'num_immatricule', 'num_bordereau', 'shipment_num', 'num_remorque', 'nom_superviseur', 'nom_gardien',
                  'nom_chauffeur', 'permis_conduire', 'num_lot', 'quality', 'grade',
                  'conformity', 'poids_theorique', 'poids_reel', 'flux']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'textinput form-control'}),
            'date_entry': forms.DateInput(attrs={'type': 'date'}),
        }
        error_messages = {
            'product': {'required': ('Ce champ est obligatoire !')},
            'warehouse': {'required': ('Ce champ est obligatoire !')},
            'client': {'required': ('Ce champ est obligatoire !')},
            'quantity': {'required': ('Ce champ est obligatoire !')},
            'date_entry': {'required': ('Ce champ est obligatoire !')},
            'carrier': {'required': ('Ce champ est obligatoire !')},
            'flux': {'required': ('Ce champ est obligatoire !')},
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_show_labels = False
        self.fields['client'].label = "Client"
        self.fields['product'].label = "Produit"
        self.fields['quantity'].label = "Quantité"
        self.fields['warehouse'].label = "Magasin"
        self.fields['date_entry'].label = "Date d'entrée"
        self.fields['num_contrat'].label = "Numéro de contrat"
        self.fields['comment'].label = "Commentaires"
        self.fields['flux'].label = "Flux (Import / Export)"
        self.fields['campagne'].label = "Campagne"
        # Transporteur
        self.fields['carrier'].label = "Identifiant transporteur"
        self.fields['num_immatricule'].label = "Numéro immatricule"
        self.fields['num_bordereau'].label = "Numéro de bordereau"
        self.fields['shipment_num'].label = "Shipment number"
        self.fields['num_remorque'].label = "Numéro de remorque"
        self.fields['nom_superviseur'].label = "Nom superviseur"
        self.fields['nom_gardien'].label = "Nom de gardien"
        self.fields['nom_chauffeur'].label = "Nom du chauffeur"
        self.fields['permis_conduire'].label = "Numéro permis de conduire"
        # Contenant
        self.fields['num_lot'].label = "Numéro de lot"
        self.fields['quality'].label = "Qualité"
        self.fields['grade'].label = "Grade"
        self.fields['conformity'].label = "Conformité"
        self.fields['poids_theorique'].label = "Poids théorique"
        self.fields['poids_reel'].label = "Poids réel"



class StockOutForm(BaseStockForm):
    class Meta(BaseStockForm.Meta):
        model = StockOut
        fields = ['product', 'warehouse', 'client', 'quantity', 'type_gestion',
                  'campagne', 'date_exit', 'num_contrat', 'comment', 'carrier',
                  'num_immatricule', 'num_bordereau', 'shipment_num', 'num_remorque', 'nom_superviseur', 'nom_gardien',
                  'nom_chauffeur', 'permis_conduire', 'num_lot', 'quality', 'grade',
                  'conformity', 'poids_theorique', 'poids_reel']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'textinput form-control'}),
            'date_exit': forms.DateInput(attrs={'type': 'date'}),
        }
        error_messages = {
            'product': {'required': ('Ce champ est obligatoire !')},
            'warehouse': {'required': ('Ce champ est obligatoire !')},
            'client': {'required': ('Ce champ est obligatoire !')},
            'quantity': {'required': ('Ce champ est obligatoire !')},
            'flux': {'required': ('Ce champ est obligatoire !')},
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_show_labels = False
        self.fields['client'].label = "Client"
        self.fields['product'].label = "Produit"
        self.fields['quantity'].label = "Quantité"
        self.fields['warehouse'].label = "Magasin"
        self.fields['date_exit'].label = "Date de sortie"
        self.fields['num_contrat'].label = "Numéro de contrat"
        self.fields['comment'].label = "Commentaires"
        self.fields['flux'].label = "Flux (Import / Export)"
        self.fields['campagne'].label = "Campagne"
        # Transporteur
        self.fields['carrier'].label = "Identifiant transporteur"
        self.fields['num_immatricule'].label = "Numéro immatricule"
        self.fields['num_bordereau'].label = "Numéro de bordereau"
        self.fields['shipment_num'].label = "Shipment number"
        self.fields['num_remorque'].label = "Numéro de remorque"
        self.fields['nom_superviseur'].label = "Nom superviseur"
        self.fields['nom_gardien'].label = "Nom de gardien"
        self.fields['nom_chauffeur'].label = "Nom du chauffeur"
        self.fields['permis_conduire'].label = "Numéro permis de conduire"
        # Contenant
        self.fields['num_lot'].label = "Numéro de lot"
        self.fields['quality'].label = "Qualité"
        self.fields['grade'].label = "Grade"
        self.fields['conformity'].label = "Conformité"
        self.fields['poids_theorique'].label = "Poids théorique"
        self.fields['poids_reel'].label = "Poids réel"
