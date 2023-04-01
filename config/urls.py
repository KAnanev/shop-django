import debug_toolbar

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from article import views

urlpatterns = [
    path('catalog/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('cart/', include('cart.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('', views.view_home, name='home')
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += staticfiles_urlpatterns()
