from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^kontakt/', views.kontakt, name="kontakt"),
    url(r'^impressum/', views.impressum, name="impressum"),
    url(r'^agb/', views.agb, name="agb"),
    url(r'^aboutUs/', views.aboutUs, name="aboutUs"),
    url(r'^umzug/', views.show, {'name': 'Umzug'}, name="umzug"),
    url(r'^reinigung/', views.show, {'name': 'Reinigung'}, name="reinigung"),
    url(r'^baufirma/', views.show, {'name': 'Baufirma'}, name="baufirma"),
    url(r'^gartenbau/', views.show, {'name': 'Gartenbau'}, name="gartenbau"),
    url(r'^immobilien/', views.show, {'name': 'Immobilien'}, name="immobilien"),
    url(r'^sanitaer/', views.show, {'name': 'Sanitaer'}, name="sanitaer"),
    url(r'^architekt/', views.show, {'name': 'Architekt'}, name="architekt"),
    url(r'^schreiner/', views.show, {'name': 'Schreiner'}, name="schreiner"),
    url(r'^maler/', views.show, {'name': 'Maler'}, name="maler"),
    url(r'^anmelden/', views.firmaForm, name="firmaForm"),
]