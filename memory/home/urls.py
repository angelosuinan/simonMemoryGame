
from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.Index.as_view(), name='index'),
            ]
with open('assets/high.txt', 'w+') as f:
    f.write("0")
