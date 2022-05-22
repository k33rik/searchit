from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('about', views.about, name='about'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='vacancies_list'),
    path('vacancy/<int:pk>/summary', views.CreateSummaryView.as_view(), name='create_summary'),
    path('', include('accounts.urls'))
]
