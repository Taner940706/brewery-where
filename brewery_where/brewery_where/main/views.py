import json
from django.views import generic as views
import urllib.request
import urllib.error


# Create your views here.
class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        brewery_name = str(self.request.GET.get('brewery_name'))

        # # source_breweries = None
        # searched_brewery = None
        data_breweries = None
        data_searched_brewery = None

        headers = {'User-Agent': 'PostmanRuntime/7.33.0'}

        try:
            url = 'https://api.openbrewerydb.org/v1/breweries'
            request = urllib.request.Request(url, headers=headers)
            source_breweries = urllib.request.urlopen(request)
            response_data = source_breweries.read()
            response_str = response_data.decode('utf-8')
            data_breweries = json.loads(response_str)
        except urllib.error.HTTPError as err:
            pass
        except KeyError as k:
            pass

        try:
            url = urllib.request.urlopen('https://api.openbrewerydb.org/v1/breweries/search?query=' + (brewery_name.replace(" ", "%20"))).read()
            request = urllib.request.Request(url, headers=headers)
            source_searched_breweries = urllib.request.urlopen(request)
            response_data = source_searched_breweries.read()
            response_str = response_data.decode('utf-8')
            data_searched_brewery = json.loads(response_str)
        except urllib.error.HTTPError as err:
            pass
        except KeyError as k:
            pass

        if data_breweries is not None:
            context['breweries'] = data_breweries

        if data_searched_brewery is not None:
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