# -*- coding: utf-8 -*-
from django import template
from ..models import Article
register = template.Library()

@register.inclusion_tag('article/randomarticles.html')
def include_random_articles():
    return {
        'random_articles': Article.objects.order_by('?')[:4]
    }
