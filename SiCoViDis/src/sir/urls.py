from django.urls import path
from . import views

app_name = "sir"

urlpatterns = [
    path('', views.sir, name='prediction_page'),
    path('sir/', views.predict_chances, name='submit_prediction'),
    #path('results/', views.view_results, name='results'),
]