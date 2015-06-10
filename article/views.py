from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Article


class ArticleListView(TemplateView):
    template_name = 'article/article_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['top_articles'] = Article.objects.order_by('-publication_date')[:4]

        if context['top_articles'].exists():
            context['latest_article'] = context['top_articles'][0]
            context['top_articles'] = context['top_articles'][1:]

        return context

class ArticleDetailView(DetailView):
    model = Article