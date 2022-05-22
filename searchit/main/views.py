from django.shortcuts import render
from django.urls import reverse_lazy

from .models import VacanciesCategory, Card, Vacancy, Summary
from django.views import generic


def home(request):
    job = VacanciesCategory.objects.all()
    card = Card.objects.all()
    return render(request, 'main/home.html', {'job': job, 'card': card})


def feedback(request):
    return render(request, 'main/feedback.html')


def about(request):
    return render(request, 'main/about.html')


class CategoryView(generic.DetailView):
    model = VacanciesCategory
    template_name = 'main/vacancies_list.html'


class CreateSummaryView(generic.CreateView):
    model = Summary
    fields = ['number', 'text']
    template_name = 'main/create_summary.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        vacancy = Vacancy.objects.get(pk=self.kwargs.get('pk'))
        form.instance.user = self.request.user
        form.instance.vacancy = vacancy
        form.save()

        return super(CreateSummaryView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancy"] = Vacancy.objects.get(id=self.kwargs.get('pk'))
        return context
