
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.detail import SingleObjectMixin

from .forms import GoodForm
from .models import Good, Category


class GoodsView(ListView):
    template_name = 'index.html'
    queryset = Good.objects.all()
    context_object_name = 'goods'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context


class GoodsListView(ListView):
    template_name = 'goods_list.html'
    queryset = Good.objects.prefetch_related('category').all()
    # queryset = Good.objects.all()
    context_object_name = 'goods'


class GoodCreateView(CreateView):
    template_name = 'good_form.html'
    form_class = GoodForm
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GoodsByCategory(SingleObjectMixin, ListView):
    template_name = 'goodbycategory_list.html'
    pk_url_kwarg = 'category_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.object
        context['categorys'] = Category.objects.all()
        context['goods'] = context['object_list']
        return context

    def get_queryset(self):
        return self.object.good_set.all()