from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


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