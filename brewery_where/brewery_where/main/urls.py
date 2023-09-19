from django.urls import path

from brewery_where.main.views import SingleView, HomeView

urlpatterns = [
    path('<int:id>/', SingleView.as_view(), name='single'),
    path('', HomeView.as_view(), name="home"),
]