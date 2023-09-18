from django.shortcuts import render
from django.views import generic as views


# Create your views here.
class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class SingleView(views.TemplateView):
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)