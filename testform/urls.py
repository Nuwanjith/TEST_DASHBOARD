from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path ('form', views.index, name='index'),
    path ('', views.form, name='form'),
    path ('excel', views.excel),
    path ('excelview', views.excelview),
    path ('submit', views.formsubmit),

]
if settings.DEBUG :
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
