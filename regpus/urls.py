from django.urls import path
from regpus.views import admin as app_admin
from regpus.views import dinkes as app_dinkes
from regpus.views import verifikator as app_verif
from regpus.views import unit as app_unit

app_name = 'regpus'
urlpatterns = [
    path('',app_admin.dashboard,name='dashboard'),
    path('need-verified/',app_admin.needverified,name='needverified'),
    path('verif/',app_admin.verifUser,name='verif'),
    path('has-verified/',app_admin.hasverified,name='verified'),
    path('dataneedverif/', app_admin.itemListViewUserNeedVerified.as_view(),name='dataneedverified'), 
    path('datahasverif/', app_admin.itemListViewUserHasVerified.as_view(),name='datahasverified'), 
]