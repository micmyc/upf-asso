from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField



class NewsIndex(NewsIndexMixin, Page):
    """
    Page qui liste les news.
    """
    subpage_types = ['news.NewsItem']


class NewsItem(AbstractNewsItem, Page):
    """
    Une news individuelle.
    """
    body = RichTextField(blank=True)

    parent_page_types = ['news.NewsIndex']
    subpage_types = []

    # Corrige l'erreur du manager
    objects = Page.objects

    # Corrige l'erreur search_fields
    search_fields = Page.search_fields + []