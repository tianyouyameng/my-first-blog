from django.conf.urls import url
from django.conf.urls import include
from blog.views import post_list
from views import post_list
urlpatterns = [
    url(r'^$', post_list, name='post_list'),
]

