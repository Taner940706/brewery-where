import json
import urllib.request
from django.views import generic as views


class Home(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        names = []
        brewery_types = []
        cities = []
        countries = []

        context = super().get_context_data(**kwargs)

        name = str(self.request.GET.get('word'))
        city = str(self.request.GET.get('city'))
        type = str(self.request.GET.get('type'))

        source_all = urllib.request(
            'https://api.openbrewerydb.org/v1/breweries').read()
        source_searched = urllib.request(
            'https://api.openbrewerydb.org/v1/breweries?by_name=' + {name} +
            '&by_city=' + {city} + '&by_type=' + {type})
        data_all = json.loads(source_all)
        data_searched = json.loads(source_searched)

        for i in range(len(data_all)):
            names.append(str(data_all[i]['name']))
            brewery_types.append(str(data_all[i]['brewery_type']))
            cities.append(str(data_all[i]['city']))
            countries.append(str(data_all[i]['country']))

        for i in range(len(data_searched)):
            names.append(str(data_searched[i]['name']))
            brewery_types.append(str(data_searched[i]['brewery_type']))
            cities.append(str(data_searched[i]['city']))
            countries.append(str(data_searched[i]['country']))

        context['names'] = names
        context['brewery_types'] = brewery_types
        context['cities'] = cities
        context['countries'] = countries

        context['breweries'] = dict(
            enumerate(
                zip(context['names'], context['brewery_types'],
                    context['cities'], context['countries'])))

        return context


class Single(views.TemplateView):
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
