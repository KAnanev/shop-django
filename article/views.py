from django.shortcuts import render

from article.models import Article


def view_home(request):
    articles = Article.objects.order_by('created')

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

