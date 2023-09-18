from django.urls import path

urlpatterns = [
    path('<int:id>/', SingleView.as_view(), name='single'),
    path('', HomeView.as_view(), name="home"),
]