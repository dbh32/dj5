from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    ordering = '-published_at'

    articles = Article.objects.order_by(ordering).prefetch_related('tag').values('id', 'title', 'text', 'image',
                                                                                 'tag__name',
                                                                                 'relationship__tag_main')

    al = []  # articles_list
    ids_list = [] # вспомогательный словарь

    for article in articles:

        if article['id'] not in ids_list:

            ids_list.append(article['id'])

            al.append({
                'id': article['id'],
                'title': article['title'],
                'text': article['text'],
                'image': article['image'],
                'scopes': [{'topic': article['tag__name'], 'is_main': article['relationship__tag_main']}],
            }
            )

        else:
            for element in al:
                if element['id'] == article['id']:
                    element['scopes'].append(
                        {'topic': article['tag__name'], 'is_main': article['relationship__tag_main']})
                    element['scopes'].sort(key=lambda x: x['is_main'], reverse=True)

    context = {
        'object_list': al,
    }

    return render(request, template, context)
