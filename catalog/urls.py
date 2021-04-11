from django.conf.urls.static import static
from django.urls import path
from catalog.views import ProductListView
from diplom_django_netology import settings


urlpatterns = [
    # path('<str:category>/<str:product>', CategoryList.as_view(), name='catalog',),
    path('<str:category>', ProductListView.as_view(), name='catalog',),
    # path('', CategoryList.as_view(), name='catalog',),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)