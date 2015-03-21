from django.views.generic.edit import CreateView, UpdateView

from .models import Kudo


class KudoCreate(CreateView):
    model = Kudo


class KudoUpdate(UpdateView):
    model = Kudo
