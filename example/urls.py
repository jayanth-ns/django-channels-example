from django.conf.urls import url
from .views import user_list, login, log_out, signup


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^$', user_list, name='user_list'),
]
