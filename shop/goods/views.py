
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import GoodForm
from .models import Good


class GoodsView(ListView):
    template_name = 'index.html'
    queryset = Good.objects.all()
    context_object_name = 'goods'


class GoodsListView(ListView):
    template_name = 'goods_list.html'
    queryset = Good.objects.all()
    context_object_name = 'goods'


class GoodCreateView(CreateView):
    template_name = 'good_form.html'
    form_class = GoodForm
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
