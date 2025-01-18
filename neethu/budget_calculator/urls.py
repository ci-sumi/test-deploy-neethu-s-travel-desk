from django.urls import path
from .import views
from .views import budget_calculator

urlpatterns = [
    path('',views.budget_calculator,name='budget_calculator')]



