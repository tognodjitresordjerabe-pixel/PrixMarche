from django import forms
from .models import Produit, Marche, Enqueteur, Affectation, Releve


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ["code_produit", "libelle", "unite"]


class MarcheForm(forms.ModelForm):
    class Meta:
        model = Marche
        fields = ["code_marche", "nom_marche", "ville"]


class EnqueteurForm(forms.ModelForm):
    class Meta:
        model = Enqueteur
        fields = ["matricule", "nom_enq", "telephone"]


class AffectationForm(forms.ModelForm):
    class Meta:
        model = Affectation
        fields = ["enqueteur", "marche", "date_debut"]
        widgets = {
            "date_debut": forms.DateInput(attrs={"type": "date"}),
        }


class ReleveForm(forms.ModelForm):
    class Meta:
        model = Releve
        fields = ["date_releve", "prix", "produit", "marche", "enqueteur"]
        widgets = {
            "date_releve": forms.DateInput(attrs={"type": "date"}),
            "prix": forms.NumberInput(attrs={"min": 1}),
        }