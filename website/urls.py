from django.conf.urls import url

from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^visitor/$', views.become_visitor, name='visitor'),
    url(r'^buyer/$', views.become_buyer, name='buyer'),
    url(r'^seller/$', views.become_seller, name='seller'),
    url(r'^place_bid/$', views.place_bid, name='place_bid'),
    url(r'^modify_bid/$', views.modify_bid, name='modify_bid'),
    url(r'^make_offer/$', views.make_offer, name='make_offer'),
    url(r'^modify_offer/$', views.modify_offer, name='modify_offer'),
]