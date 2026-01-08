print(">>> AdhesionPage chargé")

from django import forms
from django.core.mail import send_mail
from django.shortcuts import render
from django.db import models
from django.conf import settings

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class AdhesionForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=200)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)


class AdhesionPage(Page):
    # --- DÉCLARATIONS ESSENTIELLES POUR APPARAÎTRE DANS L’ADMIN ---
    parent_page_types = ["home.AssociationPage"]   # Où cette page peut être créée
    subpage_types = []                              # Elle n’a pas d’enfants
    # ----------------------------------------------------------------

    intro = RichTextField(blank=True)
    destinataires = models.CharField(
        max_length=500,
        help_text="Séparer les adresses par une virgule",
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("destinataires"),
    ]

    def serve(self, request):
        if request.method == "POST":
            form = AdhesionForm(request.POST)
            if form.is_valid():
                nom = form.cleaned_data["nom"]
                email = form.cleaned_data["email"]
                message = form.cleaned_data["message"]

                to = [a.strip() for a in self.destinataires.split(",")]

                send_mail(
                    subject=f"Nouvelle adhésion : {nom}",
                    message=f"Nom : {nom}\nEmail : {email}\nMessage :\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=to,
                )


                return render(request, "adhesion/success.html", {
                    "page": self,
                    "nom": nom,
                })

        else:
            form = AdhesionForm()

        return render(request, "adhesion/form.html", {
            "page": self,
            "form": form,
        })