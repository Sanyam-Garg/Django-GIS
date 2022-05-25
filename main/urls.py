from django.urls import path
from .views import *

urlpatterns = [
	path('', HomeView.as_view()),
	path('countries/<str:name>/', CountryView.as_view()),
	path('query/intersect-india/', IntersectIndiaView.as_view()),
]