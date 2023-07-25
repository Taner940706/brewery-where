from django.urls import path
from django_project.brewerywhere.views import Home, Single

urlpatterns = (
    path('', Home.as_view(), name='home'),
    path('<id:string>/', Single.as_view(), name='single'),
)
