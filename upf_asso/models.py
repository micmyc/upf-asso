from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.panels import FieldPanel

class AssociationPage(Page):
    raison_etre = RichTextField(blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('logo'),
        FieldPanel('raison_etre'),
    ]