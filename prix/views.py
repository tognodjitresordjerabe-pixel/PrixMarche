from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produit, Marche, Enqueteur, Affectation, Releve
from .forms import (
    ProduitForm, MarcheForm, EnqueteurForm, AffectationForm, ReleveForm
)


# ---------- ACCUEIL ----------
def accueil(request):
    compteurs = {
        "produits": Produit.objects.count(),
        "marches": Marche.objects.count(),
        "enqueteurs": Enqueteur.objects.count(),
        "affectations": Affectation.objects.count(),
        "releves": Releve.objects.count(),
    }
    return render(request, "prix/accueil.html", {"compteurs": compteurs})


# ---------- PRODUITS ----------
def produits(request):
    lignes = Produit.objects.order_by("libelle")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Produits",
        "colonnes": ["Code", "Libellé", "Unité"],
        "creer_url": "prix:produit_creer",
        "type_objet": "produit",
    })


def produit_creer(request):
    form = ProduitForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Produit créé avec succès.")
        return redirect("prix:produits")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouveau produit"
    })


def produit_modifier(request, pk):
    obj = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Produit modifié.")
        return redirect("prix:produits")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier le produit"
    })


def produit_supprimer(request, pk):
    obj = get_object_or_404(Produit, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Produit supprimé.")
        return redirect("prix:produits")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:produits"
    })


# ---------- MARCHÉS ----------
def marches(request):
    lignes = Marche.objects.order_by("nom_marche")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Marchés",
        "colonnes": ["Code", "Nom", "Ville"],
        "creer_url": "prix:marche_creer",
        "type_objet": "marche",
    })


def marche_creer(request):
    form = MarcheForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Marché créé.")
        return redirect("prix:marches")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouveau marché"
    })


def marche_modifier(request, pk):
    obj = get_object_or_404(Marche, pk=pk)
    form = MarcheForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Marché modifié.")
        return redirect("prix:marches")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier le marché"
    })


def marche_supprimer(request, pk):
    obj = get_object_or_404(Marche, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Marché supprimé.")
        return redirect("prix:marches")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:marches"
    })


# ---------- ENQUÊTEURS ----------
def enqueteurs(request):
    lignes = Enqueteur.objects.order_by("nom_enq")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Enquêteurs",
        "colonnes": ["Matricule", "Nom", "Téléphone"],
        "creer_url": "prix:enqueteur_creer",
        "type_objet": "enqueteur",
    })


def enqueteur_creer(request):
    form = EnqueteurForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Enquêteur créé.")
        return redirect("prix:enqueteurs")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouvel enquêteur"
    })


def enqueteur_modifier(request, pk):
    obj = get_object_or_404(Enqueteur, pk=pk)
    form = EnqueteurForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Enquêteur modifié.")
        return redirect("prix:enqueteurs")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier l'enquêteur"
    })


def enqueteur_supprimer(request, pk):
    obj = get_object_or_404(Enqueteur, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Enquêteur supprimé.")
        return redirect("prix:enqueteurs")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:enqueteurs"
    })


# ---------- AFFECTATIONS ----------
def affectations(request):
    lignes = Affectation.objects.select_related("enqueteur", "marche").order_by("-date_debut")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Affectations",
        "colonnes": ["Enquêteur", "Marché", "Date début"],
        "creer_url": "prix:affectation_creer",
        "type_objet": "affectation",
    })


def affectation_creer(request):
    form = AffectationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Affectation créée.")
        return redirect("prix:affectations")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouvelle affectation"
    })


def affectation_modifier(request, pk):
    obj = get_object_or_404(Affectation, pk=pk)
    form = AffectationForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Affectation modifiée.")
        return redirect("prix:affectations")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier l'affectation"
    })


def affectation_supprimer(request, pk):
    obj = get_object_or_404(Affectation, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Affectation supprimée.")
        return redirect("prix:affectations")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:affectations"
    })


# ---------- RELEVÉS ----------
def releves(request):
    lignes = Releve.objects.select_related(
        "produit", "marche", "enqueteur"
    ).order_by("-date_releve")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Relevés",
        "colonnes": ["Date", "Produit", "Marché", "Prix", "Enquêteur"],
        "creer_url": "prix:releve_creer",
        "type_objet": "releve",
    })


def releve_creer(request):
    form = ReleveForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Relevé créé.")
        return redirect("prix:releves")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouveau relevé"
    })


def releve_detail(request, pk):
    obj = get_object_or_404(
        Releve.objects.select_related("produit", "marche", "enqueteur"),
        pk=pk
    )
    return render(request, "prix/detail.html", {"releve": obj})


def releve_modifier(request, pk):
    obj = get_object_or_404(Releve, pk=pk)
    form = ReleveForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Relevé modifié.")
        return redirect("prix:releves")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier le relevé"
    })


def releve_supprimer(request, pk):
    obj = get_object_or_404(Releve, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Relevé supprimé.")
        return redirect("prix:releves")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:releves"
    })

# ---------- ENQUÊTEURS ----------
def enqueteurs(request):
    lignes = Enqueteur.objects.order_by("nom_enq")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Enquêteurs",
        "colonnes": ["Matricule", "Nom", "Téléphone"],
        "creer_url": "prix:enqueteur_creer",
        "type_objet": "enqueteur",
    })


def enqueteur_creer(request):
    form = EnqueteurForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Enquêteur créé.")
        return redirect("prix:enqueteurs")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouvel enquêteur"
    })


def enqueteur_modifier(request, pk):
    obj = get_object_or_404(Enqueteur, pk=pk)
    form = EnqueteurForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Enquêteur modifié.")
        return redirect("prix:enqueteurs")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier l'enquêteur"
    })


def enqueteur_supprimer(request, pk):
    obj = get_object_or_404(Enqueteur, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Enquêteur supprimé.")
        return redirect("prix:enqueteurs")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:enqueteurs"
    })


# ---------- AFFECTATIONS ----------
def affectations(request):
    lignes = Affectation.objects.select_related("enqueteur", "marche").order_by("-date_debut")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Affectations",
        "colonnes": ["Enquêteur", "Marché", "Date début"],
        "creer_url": "prix:affectation_creer",
        "type_objet": "affectation",
    })


def affectation_creer(request):
    form = AffectationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Affectation créée.")
        return redirect("prix:affectations")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouvelle affectation"
    })


def affectation_modifier(request, pk):
    obj = get_object_or_404(Affectation, pk=pk)
    form = AffectationForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Affectation modifiée.")
        return redirect("prix:affectations")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier l'affectation"
    })


def affectation_supprimer(request, pk):
    obj = get_object_or_404(Affectation, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Affectation supprimée.")
        return redirect("prix:affectations")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:affectations"
    })


# ---------- RELEVÉS ----------
def releves(request):
    lignes = Releve.objects.select_related(
        "produit", "marche", "enqueteur"
    ).order_by("-date_releve")
    return render(request, "prix/liste.html", {
        "lignes": lignes,
        "titre": "Relevés",
        "colonnes": ["Date", "Produit", "Marché", "Prix", "Enquêteur"],
        "creer_url": "prix:releve_creer",
        "type_objet": "releve",
    })


def releve_creer(request):
    form = ReleveForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Relevé créé.")
        return redirect("prix:releves")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Nouveau relevé"
    })


def releve_detail(request, pk):
    obj = get_object_or_404(
        Releve.objects.select_related("produit", "marche", "enqueteur"),
        pk=pk
    )
    return render(request, "prix/detail.html", {"releve": obj})


def releve_modifier(request, pk):
    obj = get_object_or_404(Releve, pk=pk)
    form = ReleveForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Relevé modifié.")
        return redirect("prix:releves")
    return render(request, "prix/formulaire.html", {
        "form": form,
        "titre": "Modifier le relevé"
    })


def releve_supprimer(request, pk):
    obj = get_object_or_404(Releve, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Relevé supprimé.")
        return redirect("prix:releves")
    return render(request, "prix/confirmer_suppression.html", {
        "objet": obj,
        "retour": "prix:releves"
    })