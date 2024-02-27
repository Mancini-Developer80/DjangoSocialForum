from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView # Per visualizzare una lista | restituisce un object_list
from forum.models import Sezione, Discussione


class HomeView(ListView):
    queryset = Sezione.objects.all()
    template_name = "core/homepage.html"
    context_object_name = "lista_sezione"

class UserList(ListView):
    model = User
    template_name = "core/users.html"


def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    discussioni_utente = Discussione.objects.filter(autore_discussione= user).order_by("-pk")
    context = { "user": user, "discussione": discussioni_utente }
    return render(request, "core/user_profile.html", context)

