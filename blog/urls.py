from django.urls import include,path
from blog.views import post_list, post_detail


urlpatterns = [
    path('', post_list),
    path('post/<int:id>/', post_detail),
]
