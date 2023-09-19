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


class View404(views.TemplateView):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['request_path'] = request.path
        return self.render_to_response(context)


class View500(views.TemplateView):
    template_name = '500.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)