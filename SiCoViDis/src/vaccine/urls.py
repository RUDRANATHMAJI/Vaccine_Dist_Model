  
from django.urls import path
from . import views

app_name = "vaccine"

urlpatterns = [
    path('vaccine', views.vaccine, name='prediction_page'),
    path('vaccine/results', views.predict_chances, name='submit_prediction'),
    #path('results/', views.view_results, name='results'),
]