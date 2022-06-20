from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.CreateFeedbackView.as_view(), name='feedback'),
    path('about', views.about, name='about'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='vacancies_list'),
    path('vacancy/<int:pk>/summary', views.CreateSummaryView.as_view(), name='create_summary'),
    path('company/create', views.CreateVacancyView.as_view(), name='create_vacancy'),
    path('', include('accounts.urls'))
]
