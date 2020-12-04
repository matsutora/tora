from django.views.generic import TemplateView,ListView
from .models import Product


class Home(TemplateView):
    template_name = 'mamazon/home.html'


class ProductListView(ListView):
    model = Product
    template_name = "mamazon/list.html"

    def get_queryset(self):
        queryset = Product.objects.all()
        if "query" in self.request.GET:
            qs = self.request.GET["query"]
            queryset = queryset.filter(name__contains=qs)
        return queryset
