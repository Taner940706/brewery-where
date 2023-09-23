import json
import urllib

from django.shortcuts import render
from django.views import generic as views
import urllib.request
import urllib.error


# Create your views here.
class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        brewery_name = str(self.request.GET.get('brewery_name'))

        source_breweries = None
        searched_brewery = None
        data_breweries = None
        data_searched_brewery = None

        try:
            source_breweries = urllib.request.urlopen('https://api.openbrewerydb.org/v1/breweries').read()
            data_breweries = json.loads(source_breweries)
        except urllib.error.HTTPError as err:
            pass
        except KeyError as k:
            pass

        try:
            searched_brewery = urllib.request.urlopen('https://api.openbrewerydb.org/v1/breweries/search?query=' + (brewery_name.replace(" ", "%20"))).read()
            data_searched_brewery = json.loads(searched_brewery)
        except urllib.error.HTTPError as err:
            pass
        except KeyError as k:
            pass

        context['breweries'] = data_breweries
        context['searched_brewery'] = data_searched_brewery

        return context


class SingleView(views.DeleteView):
    template_name = 'single.html'

    def get_object(self, queryset=None):
        brewery_id = self.kwargs.get('pk')  # 'pk' should match the URL parameter name
        brewery = self.model.objects.get(pk=brewery_id)  # Replace with your actual model logic
        return brewery


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