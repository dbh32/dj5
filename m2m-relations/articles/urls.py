from django.urls import path, include
from django.conf import settings
from articles.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),
                   ] + urlpatterns
