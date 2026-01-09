from django import forms
from django.core.mail import send_mail
from django.shortcuts import render
from django.db import models
from django.conf import settings

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    subpage_types = ['home.AssociationPage']


class AssociationPage(Page):
    parent_page_types = ['home.HomePage']

    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    raison_etre = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("raison_etre"),
    ]

    template = "home/association_page.html"

    def get_adhesion_page(self):
        from .models import AdhesionPage
        return self.get_children().type(AdhesionPage).first()



class AdhesionForm(forms.Form):
    prenom = forms.CharField(label="Prénom", max_length=200)
    nom = forms.CharField(label="Nom", max_length=200)
    email = forms.EmailField(label="Email")
    telephone = forms.CharField(label="Téléphone", max_length=20, required=False)
    message = forms.CharField(label="Message", widget=forms.Textarea)



class AdhesionPage(Page):
    class Meta:
        db_table = "pages_adhesionpage"

    parent_page_types = ["home.AssociationPage"]
    subpage_types = []

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
                prenom = form.cleaned_data["prenom"]
                nom = form.cleaned_data["nom"]
                email = form.cleaned_data["email"]
                telephone = form.cleaned_data["telephone"]
                message = form.cleaned_data["message"]
                
                to = [a.strip() for a in self.destinataires.split(",")]

                send_mail(
                    subject=f"Nouvelle adhésion : {prenom} {nom}",
                    message=(
                        f"Prénom : {prenom}\n"
                        f"Nom : {nom}\n"
                        f"Email : {email}\n"
                        f"Téléphone : {telephone}\n"
                        f"Message :\n{message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=to,
                )


                return render(request, "adhesion/success.html", {
                    "page": self,
                    "prenom": prenom,
                    "nom": nom,
                })

        else:
            form = AdhesionForm()

        return render(request, "adhesion/form.html", {
            "page": self,
            "form": form,
        })