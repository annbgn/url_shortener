from django.urls import path

from . import views

urlpatterns = [
    path('get_short', views.get_short_url_view, name='get_short'),
    path('redirect/<uuid:short_url>', views.redirect_short_url_view, name='redirect'),
]
