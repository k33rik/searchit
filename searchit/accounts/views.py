from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ProfileEditForm


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('change-password')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('profile'))

    else:
        form = ProfileEditForm(instance=request.user)
        return render(request, 'accounts/profile.html', {'form': form})
