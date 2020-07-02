
from django.conf.urls import url,include
from . import views

urlpatterns = [

    url('file_input/$', views.file_input),
    #url('sellers_input/$', views.sellers_input),
    url('order_input/$', views.order_input),
    # url('zapros/$', views.zapros),
    # url('zapr1/$', views.zapr1),

]
