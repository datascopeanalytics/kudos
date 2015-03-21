from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from .models import Kudo


# https://docs.djangoproject.com/en/1.7/topics/class-based-views/intro/#mixins-that-wrap-as-view
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class KudoCreate(LoginRequiredMixin, CreateView):
    model = Kudo


class KudoUpdate(LoginRequiredMixin, UpdateView):
    model = Kudo
