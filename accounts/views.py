from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import CreateView # type: ignore

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"