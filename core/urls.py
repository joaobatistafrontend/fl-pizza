from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import  *
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('ca/', Carrinho.as_view(), name='carrinho'),
    path('adicionar-ao-carrinho/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)