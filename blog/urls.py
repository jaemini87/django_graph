from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^cc$',views.post_list,name='post_list'),
        url(r'^$',views.view_chart,name='chart'),
]
