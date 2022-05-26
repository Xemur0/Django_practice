from django.urls import path

from .views import GoodsListView, GoodsView, GoodCreateView

urlpatterns = [
    path('', GoodsView.as_view(), name='index'),
    path('goods_list/', GoodsListView.as_view(), name='list'),
    path('add/', GoodCreateView.as_view(), name='add')

]
